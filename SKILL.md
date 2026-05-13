---
name: academical-pdf2video
description: >
  Convert an academic PDF paper into a polished 1920×1080 MP4 video with Chinese TTS narration
  (edge-tts zh-CN-XiaoxiaoNeural), background music, and a BioTender logo watermark using Remotion
  (React/TypeScript). Use this skill whenever a user uploads a scientific paper (PDF) and asks to
  render it as a video, science explainer, or short-form content — even if they say "做成视频",
  "渲染成视频", "科普视频", or "PDF转视频". Supports custom BGM (MP3), custom logo (PNG),
  adjustable video length (concise ~2min / standard ~4min / detailed ~6min), and optional
  left-image right-text layout with paper figures embedded in scenes.
---

# Academical PDF2Video

Convert any academic PDF into a narrated, animated video with Chinese TTS, background music, watermark, and optional paper figure embeds.

## Scope

Produces a 1920×1080 H.264+AAC MP4 video from a scientific PDF. Does NOT perform wet-lab analysis, statistical computation, or literature search — it is purely a science communication / video production workflow.

## Inputs

| Input | Type | Required | Notes |
|-------|------|----------|-------|
| PDF file | `.pdf` | Yes | Uploaded via `/mnt/user-uploads/` |
| BGM file | `.mp3` | No | Default: synthesize Am-F-C-G pad BGM |
| Logo file | `.png` | No | Default: text watermark "BioTender" |
| TTS voice | string | No | Default: `zh-CN-XiaoxiaoNeural` |
| TTS rate | string | No | Default: `-5%` |
| Video length | enum | No | `concise` (~2min) / `standard` (~4min) / `detailed` (~6min) |
| Embed figures | bool | No | Default: `false`. If `true`, extract paper figures and use left-image right-text layout |

## Outputs

- `biodesign_video.mp4` — 1920×1080, 30fps, H.264+AAC, saved to `/mnt/results/`
- Frame verification screenshots (cover, mid, outro) saved to `/mnt/results/`

---

## Workflow Steps

### Step 1 — Read & Summarize PDF

Read the PDF (all pages) and extract:
- **Title**, **authors**, **institution**, **venue/year**
- **Core findings** (3–5 bullet points, quantitative where possible)
- **Key figures/tables** to reference in narration
- **Narrative arc**: problem → method → results → implications

Use Claude's PDF reading capability directly. No external tools needed.

### Step 1.5 — Extract Paper Figures (optional, if embed_figures=True)

Use PyMuPDF to extract figures from the PDF:

```python
import fitz  # pip install pymupdf
import os

def extract_figures(pdf_path: str, out_dir: str, min_width: int = 400, min_height: int = 300):
    """Extract all raster images from PDF, filter by minimum size."""
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    extracted = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)
        for img_idx, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            w, h = base_image["width"], base_image["height"]
            if w < min_width or h < min_height:
                continue  # skip small icons/logos
            ext = base_image["ext"]
            fname = f"p{page_num:02d}_img{img_idx:02d}.{ext}"
            fpath = os.path.join(out_dir, fname)
            with open(fpath, "wb") as f:
                f.write(base_image["image"])
            extracted.append({"file": fname, "page": page_num, "w": w, "h": h})
            print(f"  Extracted: {fname} ({w}x{h})")
    doc.close()
    return extracted

figures = extract_figures("/mnt/user-uploads/paper.pdf", "/workspace/project/public/images/paper/")
```

**Figure-to-scene mapping** — manually assign after reviewing extracted images:
```python
# Example mapping for BioDesignBench paper
FIGURE_MAP = {
    "sc1": "p03_img00.png",   # Fig1: LLM Agent workflow
    "sc2": "p05_img00.png",   # Fig2: task taxonomy + leaderboard
    "sc3": "p05_img00.png",   # Fig2: same figure, different text
    "sc4": "p06_img00.png",   # Fig3: tool call comparison
    "sc5": "p06_img00.png",   # Fig3: same figure, different text
    "sc6": "p07_img00.png",   # Fig4: intervention results
}
```

Copy figures to Remotion public directory:
```bash
cp /workspace/figures/*.png /workspace/project/public/images/paper/
```

### Step 2 — Write Scene Scripts

Design 6–10 scenes based on video length:

| Length | Scenes | Total TTS target |
|--------|--------|-----------------|
| concise (~2min) | 6–8 | ~100–120s |
| standard (~4min) | 10–14 | ~200–240s |
| detailed (~6min) | 16–20 | ~320–360s |

**Scene structure template:**
```
sc0: Cover — hook question or bold claim (5–8s)
sc1: Background — why this problem matters (15–25s)
sc2: Method/Benchmark — what was built/tested (15–25s)
sc3: Results — key numbers, rankings, comparisons (15–25s)
sc4: Key Finding — the surprising insight (12–20s)
sc5: Data — specific quantitative evidence (12–20s)
sc6: Intervention/Validation — what confirms it (15–20s)
sc7: Outro — takeaway message (8–12s)
```

**Script writing rules:**
- Max 4 Chinese characters/second × scene duration × 0.85 safety factor
- Use concrete numbers: "14%", "+15.9分", "76个任务"
- Avoid jargon without explanation
- End with a memorable one-liner

### Step 3 — Generate TTS Audio

```python
import nest_asyncio, asyncio, edge_tts, os
nest_asyncio.apply()

VOICE = "zh-CN-XiaoxiaoNeural"  # or user-specified
RATE = "-5%"

async def gen_all(scripts: dict, out_dir: str):
    for key, text in scripts.items():
        out = f"{out_dir}/{key}.mp3"
        comm = edge_tts.Communicate(text, VOICE, rate=RATE)
        await comm.save(out)

asyncio.get_event_loop().run_until_complete(gen_all(scripts, out_dir))
```

Measure exact durations with ffprobe:
```python
import subprocess, json
def get_duration(path):
    r = subprocess.run(f'ffprobe -v quiet -print_format json -show_streams "{path}"',
                       shell=True, capture_output=True, text=True)
    return float(json.loads(r.stdout)["streams"][0]["duration"])
```

### Step 4 — Mix Audio (TTS + BGM)

```bash
# Concatenate TTS segments
ffmpeg -y -f concat -safe 0 -i concat.txt -c:a libmp3lame -q:a 2 tts_full.mp3

# Mix with BGM at 18% volume, 3s fade-in, 5s fade-out
# IMPORTANT: VIDEO_DUR = total video duration (TTS + per-scene buffers), NOT TTS duration alone
# Using apad+duration=longest ensures BGM continues after TTS ends, filling the full video length
ffmpeg -y \
  -i tts_full.mp3 \
  -i bgm.mp3 \
  -filter_complex \
    "[1:a]volume=0.18,afade=t=in:st=0:d=3,afade=t=out:st=$((VIDEO_DUR-5)):d=5,atrim=0:${VIDEO_DUR},apad=whole_dur=${VIDEO_DUR}[bgm];
     [0:a]apad=whole_dur=${VIDEO_DUR}[tts];
     [tts][bgm]amix=inputs=2:duration=longest:dropout_transition=3[out]" \
  -map "[out]" \
  -t ${VIDEO_DUR} \
  -c:a libmp3lame -q:a 2 audio_final.mp3
# VIDEO_DUR example: TTS=119.9s, per-scene buffer=2.5s x 8 scenes → VIDEO_DUR=141s
```

**If no BGM provided**, synthesize programmatically:
```python
import numpy as np
from scipy.io import wavfile
# Am-F-C-G chord pad at 72 BPM, -18 dBFS
# See previous session notes for full synthesis code
```

### Step 5 — Process Logo

```python
from PIL import Image
import numpy as np

img = Image.open(logo_path).convert("RGBA")
arr = np.array(img)
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
brightness = (r.astype(int) + g.astype(int) + b.astype(int)) / 3

# Convert black-on-white logo to white-on-transparent
new_arr = np.zeros_like(arr)
new_arr[:,:,0] = 255  # white
new_arr[:,:,1] = 255
new_arr[:,:,2] = 255
new_arr[:,:,3] = (255 - brightness).astype(np.uint8)

Image.fromarray(new_arr).save("logo_white.png")
```

### Step 6 — Build Remotion Project

**Environment setup:**
```bash
# Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs ffmpeg chromium fonts-noto-cjk

# Remotion
npm init -y
npm install --save-exact remotion@4.0.290 @remotion/cli@4.0.290 @remotion/renderer@4.0.290 react@18.3.1 react-dom@18.3.1
npm install --save-dev typescript @types/react @types/react-dom
```

**package.json remotion field:**
```json
{
  "remotion": { "entrypoint": "src/index.ts" }
}
```

**Critical files:**
- `src/index.ts` — must call `registerRoot(RemotionRoot)`
- `src/Root.tsx` — `<Composition>` + `<Series>` + global `<Audio src={staticFile("audio/bgm_mixed.mp3")} />` (BGM only)
- `src/loadFonts.ts` — inject `@font-face` for Noto Serif CJK SC from `staticFile("fonts/...")`
- `src/BioTenderLogo.tsx` — `position: absolute, bottom: 32, right: 40`, all scenes
- `src/scenes.tsx` — 6–10 scene components, each with `<Audio src={staticFile("audio/scX.mp3")} />` inside

**CRITICAL — Audio architecture (two separate tracks):**
```
Root.tsx:   <Audio src={staticFile("audio/bgm_mixed.mp3")} />   ← BGM only, 141s, global
Scene0:     <Audio src={staticFile("audio/sc0.mp3")} />          ← TTS per scene
Scene1:     <Audio src={staticFile("audio/sc1.mp3")} />
...
Scene7:     <Audio src={staticFile("audio/sc7.mp3")} />
```
**Why**: Each scene has a 2.5s buffer after TTS ends. If all TTS is concatenated into one global track, the cumulative buffer offset (8 scenes × 2.5s = 20s) causes sc7 TTS to play 20s before sc7 appears on screen — the viewer hears silence during the last scene. Per-scene audio fires exactly when each scene starts, eliminating the offset problem entirely.

**BGM-only track preparation:**
```bash
VIDEO_DUR=141  # total video duration in seconds
ffmpeg -y \
  -i bgm.mp3 \
  -filter_complex "[0:a]volume=0.18,afade=t=in:st=0:d=3,afade=t=out:st=$((VIDEO_DUR-5)):d=5,atrim=0:${VIDEO_DUR}[out]" \
  -map "[out]" -t ${VIDEO_DUR} -c:a libmp3lame -q:a 2 bgm_mixed.mp3
```

**Scene frame calculation:**
```python
import math
FPS = 30
BUFFER = 2.5  # seconds after TTS ends

for key, tts_dur in durations.items():
    frames = math.ceil((tts_dur + BUFFER) * FPS / 10) * 10  # round up to 10 frames
```

**Font loading (critical for headless Chrome):**
```typescript
// src/loadFonts.ts
import { staticFile } from "remotion";
export function loadFonts() {
  if (typeof document === "undefined") return;
  const style = document.createElement("style");
  style.textContent = `
    @font-face {
      font-family: 'Noto Serif SC';
      font-weight: 400;
      src: url('${staticFile("fonts/NotoSerifSC-Regular.ttc")}') format('truetype');
    }
  `;
  document.head.appendChild(style);
}
// Call loadFonts() at module level in Root.tsx
```

**SplitLayout component (for left-image right-text scenes):**
```tsx
// In src/scenes.tsx
import { useCurrentFrame, useVideoConfig, spring, staticFile, Img } from "remotion";

interface SplitLayoutProps {
  imageSrc: string;       // e.g. staticFile("images/paper/p03_img00.png")
  children: React.ReactNode;  // right-side text content
}

const SplitLayout: React.FC<SplitLayoutProps> = ({ imageSrc, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const imgOpacity = spring({ frame, fps, from: 0, to: 1, config: { damping: 20 } });
  const imgScale = spring({ frame, fps, from: 0.92, to: 1, config: { damping: 18 } });

  return (
    <div style={{ display: "flex", width: "100%", height: "100%", alignItems: "center", padding: "60px 80px", gap: 60 }}>
      {/* Left panel: 52% width */}
      <div style={{
        flex: "0 0 52%",
        opacity: imgOpacity,
        transform: `scale(${imgScale})`,
        background: "rgba(255,255,255,0.97)",
        borderRadius: 20,
        padding: 16,
        boxShadow: "0 0 40px rgba(100,180,255,0.35), 0 8px 32px rgba(0,0,0,0.4)",
        display: "flex", alignItems: "center", justifyContent: "center",
        maxHeight: "75%",
        overflow: "hidden",
      }}>
        <Img src={imageSrc} style={{ width: "100%", height: "auto", objectFit: "contain", borderRadius: 12 }} />
      </div>
      {/* Right panel: 48% width */}
      <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center" }}>
        {children}
      </div>
    </div>
  );
};

// Usage in a scene:
export const SceneBackground: React.FC<{ durationInFrames: number }> = ({ durationInFrames }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const textOpacity = spring({ frame: frame - 15, fps, from: 0, to: 1, config: { damping: 20 } });

  return (
    <div style={{ width: "100%", height: "100%", background: "linear-gradient(135deg, #0a1628 0%, #0d2040 100%)", position: "relative" }}>
      <BioTenderLogo />
      <SplitLayout imageSrc={staticFile("images/paper/p03_img00.png")}>
        <div style={{ opacity: textOpacity, color: "#7ec8e3", fontSize: 22, letterSpacing: 8, marginBottom: 20 }}>
          § 01 · 背 景
        </div>
        <div style={{ color: "#ffffff", fontSize: 52, fontWeight: 700, lineHeight: 1.3, marginBottom: 28 }}>
          LLM Agent ×{"\n"}蛋白质设计工具链
        </div>
        <div style={{ color: "rgba(255,255,255,0.75)", fontSize: 26, lineHeight: 1.7 }}>
          大语言模型被赋予工具调用能力，<br />可自主完成从头蛋白质设计任务。
        </div>
      </SplitLayout>
    </div>
  );
};
```

**DO NOT use emoji** in scene components — headless Chromium has no emoji font. Use unicode geometric symbols (◈ ◉ ◆ ◎ ▶ ✓ ✗) instead.

### Step 7 — Render

```bash
cd /workspace/<project> && \
npx remotion render BioDesignBench \
  --concurrency=1 \
  --output=/workspace/output.mp4 \
  --browser-executable=$(which chromium)
```

**Verify test frame first:**
```bash
npx remotion still BioDesignBench --frame=150 --output=/tmp/test.png --browser-executable=$(which chromium)
```

### Step 8 — Quality Verification

Extract frames at cover / mid / outro:
```bash
ffmpeg -ss 4 -i output.mp4 -frames:v 1 /tmp/sc0.png -y
ffmpeg -ss 20 -i output.mp4 -frames:v 1 /tmp/sc1.png -y
ffmpeg -ss 70 -i output.mp4 -frames:v 1 /tmp/sc4.png -y
ffmpeg -ss 135 -i output.mp4 -frames:v 1 /tmp/sc7.png -y
```

Check with `Read(mode="low")`:
- Chinese characters render without tofu boxes
- BioTender watermark visible bottom-right
- Left-image right-text layout: paper figure visible in left panel, Chinese text in right panel
- Animations smooth (no frozen frames)
- Audio present (file size > 5 MB for ~2min video, > 10 MB if figures embedded)

Copy to results:
```bash
cp /workspace/output.mp4 /mnt/results/biodesign_video.mp4
```

---

## Scientific Caveats

- **Scores shown in leaderboard scenes must be verified** against paper tables/figures. Always use exact values from the paper, not approximations.
- **TTS narration is AI-generated** — verify technical terms are pronounced correctly (e.g., "RFdiffusion", "ProteinMPNN").
- **Font rendering**: Noto Serif CJK SC covers Simplified Chinese. For Traditional Chinese, use `NotoSerifCJK-TC`. For Japanese/Korean, use respective variants.
- **BGM copyright**: User-provided MP3 may have copyright restrictions. Programmatically synthesized BGM (Am-F-C-G pad) is copyright-free.
- **Figure extraction**: PyMuPDF extracts raster images embedded in PDF. Vector figures (SVG/PDF-native) may not be extracted. Use `min_width=400, min_height=300` to filter out icons and logos.

---

## Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `registerRoot not found` | `src/index.ts` must call `registerRoot(RemotionRoot)` |
| Chinese tofu boxes | Install `fonts-noto-cjk` via apt; use `loadFonts()` with `staticFile()` paths |
| Emoji boxes | Replace all emoji with unicode geometric symbols |
| Audio silent after 2:00 (TTS) | Never concatenate all TTS into one global audio track — per-scene buffer frames accumulate offset. Use per-scene `<Audio src={staticFile("audio/scX.mp3")} />` inside each Scene component so TTS fires exactly when the scene starts |
| Audio silent after 2:00 (BGM) | `duration=first` truncates BGM to TTS length; use `apad=whole_dur=VIDEO_DUR` + `duration=longest` so BGM fills full video |
| Audio not synced | TTS: per-scene `<Audio>` in each Scene component. BGM: single global `<Audio>` in Root pointing to BGM-only track |
| `asyncio.run()` error in Jupyter | Add `import nest_asyncio; nest_asyncio.apply()` before async calls |
| Font CDN fails in headless | Copy font files to `public/fonts/`, serve via `staticFile()` |
| Figure not showing in SplitLayout | Ensure image is in `public/images/paper/` and referenced via `staticFile()` |
| PyMuPDF extracts wrong images | Increase `min_width`/`min_height` thresholds; inspect extracted files manually |

---

## Example Trigger Prompts

- "看一下这篇PDF，然后渲染成视频，用edge tts的中文普通话女声"
- "把这篇论文做成科普视频，加上BioTender水印"
- "Convert this paper to a 2-minute explainer video in Chinese"
- "这篇bioRxiv文章能做成短视频吗？"
- "放一些文章图片在视频里面，可以做成左图右字" (triggers embed_figures=True + SplitLayout)
