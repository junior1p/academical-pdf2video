---
name: academical-pdf2video
description: >
  Convert an academic PDF paper (or HTML article) into a polished 1920×1080 MP4 video with
  AI narration, background music, and a BioTender logo watermark. Supports multiple TTS engines
  (edge-tts, F5-TTS voice cloning, CosyVoice2, Kokoro), two rendering backends (Remotion React/TypeScript
  or HyperFrames HTML/GSAP), bilingual output (Chinese/English), subtitles (ASS/SRT), vertical
  (1080×1920) and landscape (1920×1080) formats, and optional paper figure embeds with left-image
  right-text layout. Use this skill whenever a user uploads a scientific paper (PDF or HTML) and
  asks to render it as a video, science explainer, or short-form content — even if they say
  "做成视频", "渲染成视频", "科普视频", "PDF转视频", "做个短视频", or "convert to video".
---

# Academical PDF2Video

Convert any academic PDF or HTML article into a narrated, animated video with AI TTS, background music, watermark, subtitles, and optional paper figure embeds.

---

## Scope

Produces a 1920×1080 (or 1080×1920 vertical) H.264+AAC MP4 video from a scientific PDF or HTML article. Does NOT perform wet-lab analysis, statistical computation, or literature search — it is purely a science communication / video production workflow.

---

## Inputs

| Input | Type | Required | Notes |
|-------|------|----------|-------|
| Source file | `.pdf` or `.html` | Yes | Uploaded via `/mnt/user-uploads/` |
| BGM file | `.mp3` | No | Default: synthesize Am-F-C-G pad BGM |
| Logo file | `.png` | No | Default: text watermark "BioTender" |
| TTS engine | enum | No | `edge-tts` (default) / `f5-tts` / `cosyvoice2` / `kokoro` |
| TTS voice | string | No | See TTS Voice Reference below |
| TTS rate | string | No | Default: `-5%` (edge-tts) |
| Language | enum | No | `zh` (default) / `en` / `bilingual` |
| Video length | enum | No | `concise` (~2min) / `standard` (~4min) / `detailed` (~6min) |
| Orientation | enum | No | `landscape` 1920×1080 (default) / `vertical` 1080×1920 |
| Embed figures | bool | No | Default: `false`. If `true`, extract paper figures and use left-image right-text layout |
| Subtitles | bool | No | Default: `false`. If `true`, burn ASS/SRT subtitles into video |
| Render backend | enum | No | `remotion` (default) / `hyperframes` / `playwright` |
| Reference voice | `.wav/.m4a` | No | Required for F5-TTS / CosyVoice2 voice cloning |

---

## Outputs

- `<paper_name>_video.mp4` — 1920×1080 (or 1080×1920), 30fps, H.264+AAC, saved to `/mnt/results/`
- Frame verification screenshots saved to `/mnt/results/`
- Optional: subtitle file (`.ass` or `.srt`)

---

## TTS Engine Selection Guide

| Engine | Best For | Languages | Voice Cloning | Speed | Install |
|--------|----------|-----------|---------------|-------|---------|
| **edge-tts** | Quick, reliable, no GPU | 74 languages, 322 voices | No | Very fast | `pip install edge-tts` |
| **F5-TTS** | Custom voice cloning, CPU-ok | ZH + EN | Yes (5s sample) | Slow on CPU (~18x RTF) | Local weights |
| **CosyVoice2** | Emotion/dialect control, streaming | ZH/EN/JP/KR/DE/FR/ES/IT/RU | Yes | Fast (GPU) | Local weights |
| **Kokoro** | Lightweight, fast, no cloning | 9 languages | No | Very fast | `pip install kokoro-onnx` |
| **GPT-SoVITS** | Highest quality cloning | ZH/EN/JP/KR/Cantonese | Yes (5s) | Medium | Local weights |

### edge-tts Voice Reference

**Chinese (Simplified) — zh-CN:**
| Voice ID | Name | Style | Best For |
|----------|------|-------|----------|
| `zh-CN-XiaoxiaoNeural` | 晓晓 | Warm, natural | Science explainers (default) |
| `zh-CN-XiaoyiNeural` | 晓伊 | Sweet, lively | Youth content |
| `zh-CN-YunxiNeural` | 云希 | Male, energetic | Tech/startup content |
| `zh-CN-YunyangNeural` | 云扬 | Male, news anchor | Formal/news style |
| `zh-CN-XiaohanNeural` | 晓涵 | Elegant | Academic/documentary |
| `zh-CN-XiaomengNeural` | 晓梦 | Dreamy | Creative content |
| `zh-CN-XiaochenNeural` | 晓辰 | Intellectual | Research papers |
| `zh-CN-XiaoruiNeural` | 晓睿 | Senior female | Authoritative |
| `zh-CN-XiaoshuangNeural` | 晓双 | Child-like | Education |
| `zh-CN-YunjianNeural` | 云健 | Male, sports | Dynamic content |
| `zh-CN-YunxiaNeural` | 云夏 | Male, young | Casual explainers |
| `zh-CN-XiaobeiNeural` | 晓北 | Northeastern dialect | Regional content |
| `zh-CN-liaoning-XiaobeiNeural` | 晓北(辽宁) | Liaoning dialect | — |
| `zh-CN-shaanxi-XiaoniNeural` | 晓妮(陕西) | Shaanxi dialect | — |

**Chinese (Traditional/HK) — zh-HK / zh-TW:**
| Voice ID | Notes |
|----------|-------|
| `zh-HK-HiuGaaiNeural` | Cantonese female |
| `zh-HK-HiuMaanNeural` | Cantonese female |
| `zh-HK-WanLungNeural` | Cantonese male |
| `zh-TW-HsiaoChenNeural` | Taiwan Mandarin female |
| `zh-TW-HsiaoYuNeural` | Taiwan Mandarin female |
| `zh-TW-YunJheNeural` | Taiwan Mandarin male |

**English — en-US / en-GB / en-AU:**
| Voice ID | Style |
|----------|-------|
| `en-US-JennyNeural` | Friendly female (default EN) |
| `en-US-AriaNeural` | Natural female |
| `en-US-GuyNeural` | Natural male |
| `en-US-EmmaMultilingualNeural` | Multilingual female |
| `en-US-AndrewMultilingualNeural` | Multilingual male |
| `en-GB-SoniaNeural` | British female |
| `en-AU-NatashaNeural` | Australian female |

**Japanese — ja-JP:**
| Voice ID | Notes |
|----------|-------|
| `ja-JP-NanamiNeural` | Female |
| `ja-JP-KeitaNeural` | Male |

**Korean — ko-KR:**
| Voice ID | Notes |
|----------|-------|
| `ko-KR-SunHiNeural` | Female |
| `ko-KR-InJoonNeural` | Male |

**Other Notable Languages:**
| Voice ID | Language |
|----------|----------|
| `fr-FR-DeniseNeural` | French female |
| `de-DE-KatjaNeural` | German female |
| `es-ES-ElviraNeural` | Spanish female |
| `pt-BR-FranciscaNeural` | Portuguese (Brazil) female |
| `ar-SA-ZariyahNeural` | Arabic female |
| `hi-IN-SwaraNeural` | Hindi female |

### edge-tts Style Modifiers (SSML)

```python
# Apply speaking style via SSML
text_with_style = """
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis'
       xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='zh-CN'>
  <voice name='zh-CN-XiaoxiaoNeural'>
    <mstts:express-as style='newscast-casual' styledegree='1.5'>
      今天我们来聊一聊蛋白质设计的最新进展。
    </mstts:express-as>
  </voice>
</speak>
"""
# Available styles for XiaoxiaoNeural: general, newscast-casual, newscast-formal,
# customerservice, chat, cheerful, empathetic, lyrical, poetry-reading
```

---

## Rendering Backend Selection Guide

| Backend | Best For | Authoring | License | Node.js | Complexity |
|---------|----------|-----------|---------|---------|------------|
| **Remotion** | Data-driven scenes, React components, charts | React/TSX | Source-available (free <3 seats) | 20+ | Medium |
| **HyperFrames** | Kinetic typography, HTML articles, AI-generated | HTML+GSAP | Apache 2.0 | 22+ | Low |
| **Playwright** | Simple slides, no Node.js available | HTML+CSS | Apache 2.0 | Not needed | Low |

### When to Use Each Backend

**Use Remotion when:**
- You need reusable React components (stat cards, bar charts, leaderboards)
- You have complex data-driven animations
- You want TypeScript type safety
- You're building a series of similar videos

**Use HyperFrames when:**
- Source is an HTML article (convert directly)
- You want AI agents to write the composition (HTML is more LLM-friendly)
- You need kinetic typography or GSAP-native animations
- You want Apache 2.0 license (commercial use at any scale)

**Use Playwright when:**
- Node.js is not available
- Simple slide-based content
- Quick prototyping

---

## Workflow Steps

### Step 1 — Read & Summarize Source

**For PDF:**
```python
import fitz  # pymupdf
doc = fitz.open("/mnt/user-uploads/paper.pdf")
text = "\n".join([page.get_text() for page in doc])
```
Or use Claude's native PDF reading capability directly.

Extract:
- **Title**, **authors**, **institution**, **venue/year**
- **Core findings** (3–5 bullet points, quantitative where possible)
- **Key figures/tables** to reference in narration
- **Narrative arc**: problem → method → results → implications

**For HTML:**
```python
from bs4 import BeautifulSoup
with open("/mnt/user-uploads/article.html", "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")
text = soup.get_text(separator="\n", strip=True)
```

### Step 1.5 — Extract Figures (optional, if embed_figures=True)

**From PDF (PyMuPDF):**
```python
import fitz, os

def extract_figures(pdf_path: str, out_dir: str, min_width: int = 400, min_height: int = 300):
    os.makedirs(out_dir, exist_ok=True)
    doc = fitz.open(pdf_path)
    extracted = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        for img_idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            w, h = base_image["width"], base_image["height"]
            if w < min_width or h < min_height:
                continue
            ext = base_image["ext"]
            fname = f"p{page_num:02d}_img{img_idx:02d}.{ext}"
            fpath = os.path.join(out_dir, fname)
            with open(fpath, "wb") as f:
                f.write(base_image["image"])
            extracted.append({"file": fname, "page": page_num, "w": w, "h": h})
    doc.close()
    return extracted

figures = extract_figures("/mnt/user-uploads/paper.pdf", "/workspace/project/public/images/paper/")
```

**From HTML (base64 images):**
```python
import base64, re, os
from bs4 import BeautifulSoup

def extract_html_images(html_path: str, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    with open(html_path, "r") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
    extracted = []
    for i, img in enumerate(soup.find_all("img")):
        src = img.get("src", "")
        if src.startswith("data:image"):
            match = re.match(r"data:image/(\w+);base64,(.+)", src)
            if match:
                ext, data = match.group(1), match.group(2)
                fname = f"img_{i:02d}.{ext}"
                with open(os.path.join(out_dir, fname), "wb") as f:
                    f.write(base64.b64decode(data))
                extracted.append({"file": fname, "alt": img.get("alt", ""), "index": i})
    return extracted
```

**Figure-to-scene mapping:**
```python
FIGURE_MAP = {
    "sc1": "p03_img00.png",   # Fig1: method overview
    "sc2": "p05_img00.png",   # Fig2: benchmark results
    "sc3": "p06_img00.png",   # Fig3: key finding
    "sc4": "p07_img00.png",   # Fig4: validation
}
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
- **Chinese**: Max 4 characters/second × scene duration × 0.85 safety factor
- **English**: Max 2.5 words/second × scene duration × 0.85 safety factor
- Use concrete numbers: "14%", "+15.9分", "76个任务"
- Avoid jargon without explanation
- End with a memorable one-liner
- **DO NOT use emoji** in scripts — headless Chromium has no emoji font

### Step 3 — Generate TTS Audio

#### Option A: edge-tts (recommended, no GPU needed)

```python
import nest_asyncio, asyncio, edge_tts, os
nest_asyncio.apply()

VOICE = "zh-CN-XiaoxiaoNeural"  # change as needed
RATE = "-5%"   # range: -50% to +100%
PITCH = "+0Hz" # range: -50Hz to +50Hz

async def gen_all(scripts: dict, out_dir: str):
    os.makedirs(out_dir, exist_ok=True)
    for key, text in scripts.items():
        out = f"{out_dir}/{key}.mp3"
        comm = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
        await comm.save(out)
        print(f"Generated: {out}")

asyncio.get_event_loop().run_until_complete(gen_all(scripts, "/workspace/audio"))
```

**Generate with word-boundary subtitles:**
```python
async def gen_with_subtitles(text: str, voice: str, out_mp3: str, out_srt: str):
    comm = edge_tts.Communicate(text, voice, rate="-5%")
    submaker = edge_tts.SubMaker()
    with open(out_mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
    with open(out_srt, "w", encoding="utf-8") as f:
        f.write(submaker.get_srt())
```

#### Option B: F5-TTS (voice cloning, CPU-compatible)

```python
# Prerequisites: pip install f5-tts
# Local weights: /root/.cache/huggingface/hub/models--SWivid--F5-TTS/
import subprocess

def f5_tts_generate(text: str, ref_audio: str, out_wav: str,
                    nfe_step: int = 16, speed: float = 1.0):
    """
    ref_audio: 5-30s WAV/M4A of target voice
    nfe_step: 16 (fastest) to 32 (best quality)
    RTF on CPU: ~18x (89s to generate 4.9s audio)
    RTF on GPU: ~0.15x (near real-time)
    """
    cmd = [
        "f5-tts_infer-cli",
        "--model", "F5TTS_v1_Base",
        "--ref_audio", ref_audio,
        "--ref_text", "",  # auto-transcribe with Whisper
        "--gen_text", text,
        "--output_file", out_wav,
        "--nfe_step", str(nfe_step),
        "--speed", str(speed),
        "--remove_silence",
    ]
    subprocess.run(cmd, check=True)

# Batch generation
for key, text in scripts.items():
    f5_tts_generate(text, "/workspace/reference_voice.wav",
                    f"/workspace/audio/{key}_f5.wav")
```

**F5-TTS performance notes:**
- CPU RTF ≈ 18x (very slow for long scripts — use GPU if available)
- GPU RTF ≈ 0.15x (near real-time)
- Long text (>200 chars) may cause instability ("核嗓" issue) — split into shorter segments
- Model size: F5TTS_v1_Base = 1286MB + vocos vocoder = 52MB

#### Option C: CosyVoice2 (emotion/dialect control)

```python
# pip install cosyvoice
# Supports: zh/en/jp/ko/de/fr/es/it/ru + 18 Chinese dialects
from cosyvoice.cli.cosyvoice import CosyVoice2
from cosyvoice.utils.file_utils import load_wav
import torchaudio

cosyvoice = CosyVoice2('pretrained_models/CosyVoice2-0.5B',
                        load_jit=False, load_trt=False)

# Zero-shot voice cloning
prompt_speech_16k = load_wav('/workspace/reference_voice.wav', 16000)
for i, j in enumerate(cosyvoice.inference_zero_shot(
    '今天我们来聊一聊蛋白质设计的最新进展。',
    '这是参考音频的文本内容。',
    prompt_speech_16k, stream=False
)):
    torchaudio.save(f'/workspace/audio/sc{i}.wav', j['tts_speech'], cosyvoice.sample_rate)

# Instruct mode (emotion/style control)
for i, j in enumerate(cosyvoice.inference_instruct2(
    '今天我们来聊一聊蛋白质设计的最新进展。',
    '用激动的语气说',  # instruction
    prompt_speech_16k, stream=False
)):
    torchaudio.save(f'/workspace/audio/sc{i}_instruct.wav', j['tts_speech'], cosyvoice.sample_rate)
```

**CosyVoice2 dialect instructions:**
```python
# Dialect examples
dialects = {
    "普通话": "用普通话说",
    "粤语": "用粤语说",
    "四川话": "用四川话说",
    "上海话": "用上海话说",
    "东北话": "用东北话说",
}
```

#### Option D: Kokoro (lightweight, fast, no GPU)

```python
# pip install kokoro-onnx soundfile
from kokoro_onnx import Kokoro
import soundfile as sf

kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")

# Available Chinese voices: zf_001 (female), zm_001 (male)
# Available English voices: af_heart, af_bella, am_adam, am_michael, bf_emma, bm_george
samples, sample_rate = kokoro.create(
    "今天我们来聊一聊蛋白质设计的最新进展。",
    voice="zf_001",
    speed=1.0,
    lang="cmn"  # cmn=Mandarin, en-us=English, ja=Japanese, ko=Korean
)
sf.write("/workspace/audio/sc1.wav", samples, sample_rate)
```

### Step 4 — Measure TTS Durations

```python
import subprocess, json

def get_duration(path: str) -> float:
    r = subprocess.run(
        f'ffprobe -v quiet -print_format json -show_streams "{path}"',
        shell=True, capture_output=True, text=True
    )
    streams = json.loads(r.stdout).get("streams", [])
    return float(streams[0]["duration"]) if streams else 0.0

durations = {key: get_duration(f"/workspace/audio/{key}.mp3")
             for key in scripts.keys()}
print(durations)
```

### Step 5 — Mix Audio (TTS + BGM)

```bash
# Concatenate TTS segments
cat > /workspace/concat.txt << EOF
file '/workspace/audio/sc0.mp3'
file '/workspace/audio/sc1.mp3'
...
EOF
ffmpeg -y -f concat -safe 0 -i /workspace/concat.txt -c:a libmp3lame -q:a 2 /workspace/tts_full.mp3

# Mix with BGM at 18% volume, 3s fade-in, 5s fade-out
VIDEO_DUR=141  # TTS total + per-scene buffers
ffmpeg -y \
  -i /workspace/tts_full.mp3 \
  -i /workspace/bgm.mp3 \
  -filter_complex \
    "[1:a]volume=0.18,afade=t=in:st=0:d=3,afade=t=out:st=$((VIDEO_DUR-5)):d=5,atrim=0:${VIDEO_DUR},apad=whole_dur=${VIDEO_DUR}[bgm];
     [0:a]apad=whole_dur=${VIDEO_DUR}[tts];
     [tts][bgm]amix=inputs=2:duration=longest:dropout_transition=3[out]" \
  -map "[out]" -t ${VIDEO_DUR} -c:a libmp3lame -q:a 2 /workspace/audio_final.mp3
```

**BGM-only track (for Remotion per-scene audio architecture):**
```bash
VIDEO_DUR=141
ffmpeg -y \
  -i bgm.mp3 \
  -filter_complex "[0:a]volume=0.18,afade=t=in:st=0:d=3,afade=t=out:st=$((VIDEO_DUR-5)):d=5,atrim=0:${VIDEO_DUR}[out]" \
  -map "[out]" -t ${VIDEO_DUR} -c:a libmp3lame -q:a 2 /workspace/bgm_mixed.mp3
```

**Synthesize BGM programmatically (no copyright):**
```python
import numpy as np
from scipy.io import wavfile

def synthesize_bgm(duration_s: float, out_path: str, bpm: int = 72,
                   target_dbfs: float = -18.0):
    """Am-F-C-G chord pad + pulse + arpeggio shimmer"""
    sr = 44100
    t = np.linspace(0, duration_s, int(sr * duration_s))
    # Am-F-C-G chord roots (Hz)
    chord_roots = [220.0, 174.6, 261.6, 196.0]
    beat_dur = 60.0 / bpm
    signal = np.zeros_like(t)
    for i, root in enumerate(chord_roots):
        start = int(i * beat_dur * 2 * sr)
        end = int((i + 1) * beat_dur * 2 * sr)
        if end > len(t): end = len(t)
        # Pad chord (root + 3rd + 5th)
        for harmonic in [1.0, 1.26, 1.5]:
            freq = root * harmonic
            env = np.exp(-0.5 * np.linspace(0, 1, end - start))
            signal[start:end] += 0.3 * env * np.sin(2 * np.pi * freq * t[start:end])
    # Normalize to target dBFS
    peak = np.max(np.abs(signal))
    if peak > 0:
        target_amp = 10 ** (target_dbfs / 20)
        signal = signal * (target_amp / peak)
    # Fade in/out
    fade_samples = int(3 * sr)
    signal[:fade_samples] *= np.linspace(0, 1, fade_samples)
    signal[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    wavfile.write(out_path, sr, (signal * 32767).astype(np.int16))
```

### Step 6 — Build Subtitle Track (optional)

**ASS format (for ffmpeg burn-in):**
```python
def build_ass_subtitles(scenes: list, out_path: str,
                        font_size: int = 38, play_res: tuple = (1920, 1080)):
    """
    scenes: [{"start": 5.0, "text": "今天我们来聊...", "duration": 20.0}, ...]
    """
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {play_res[0]}
PlayResY: {play_res[1]}
Timer: 100.0000

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,Noto Sans CJK SC,{font_size},&H00FFFFFF,&H000000FF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2,1,2,10,10,20,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    def fmt_time(s: float) -> str:
        h = int(s // 3600)
        m = int((s % 3600) // 60)
        sec = s % 60
        return f"{h}:{m:02d}:{sec:05.2f}"

    events = []
    for scene in scenes:
        start = scene["start"]
        end = start + scene["duration"]
        text = scene["text"].replace("\n", "\\N")
        events.append(f"Dialogue: 0,{fmt_time(start)},{fmt_time(end)},Default,,0,0,0,,{text}")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(header + "\n".join(events))
```

**Burn subtitles with ffmpeg:**
```bash
ffmpeg -y -i output_silent.mp4 \
  -vf "subtitles=/workspace/subtitles.ass:fontsdir=/usr/share/fonts" \
  -c:a copy output_with_subs.mp4
```

### Step 7A — Render with Remotion

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

**Critical file structure:**
```
src/
  index.ts          ← registerRoot(RemotionRoot)
  Root.tsx          ← <Composition> + <Series> + global BGM <Audio>
  loadFonts.ts      ← inject @font-face for Noto Serif CJK SC
  BioTenderLogo.tsx ← watermark component
  scenes.tsx        ← 6-10 scene components
public/
  audio/
    bgm_mixed.mp3   ← BGM-only track
    sc0.mp3 ... scN.mp3  ← per-scene TTS
  fonts/
    NotoSerifSC-Regular.ttc
  images/paper/     ← extracted figures (if embed_figures=True)
```

**CRITICAL — Audio architecture (two separate tracks):**
```
Root.tsx:   <Audio src={staticFile("audio/bgm_mixed.mp3")} />   ← BGM only, global
Scene0:     <Audio src={staticFile("audio/sc0.mp3")} />          ← TTS per scene
Scene1:     <Audio src={staticFile("audio/sc1.mp3")} />
...
SceneN:     <Audio src={staticFile("audio/scN.mp3")} />
```
**Why**: Each scene has a 2.5s buffer after TTS ends. If all TTS is concatenated into one global track, the cumulative buffer offset (N scenes × 2.5s) causes later scenes' TTS to play before those scenes appear. Per-scene audio fires exactly when each scene starts.

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

**Alternative: embed fonts as base64 (most reliable):**
```typescript
// src/fontData.ts — pre-generate with Python
// python3 -c "import base64; print(base64.b64encode(open('NotoSerifSC-Regular.ttc','rb').read()).decode())" > font_b64.txt
export const NOTO_SERIF_SC_B64 = "AAAAAA..."; // base64 string

export function injectFonts() {
  if (typeof document === "undefined") return;
  const style = document.createElement("style");
  style.textContent = `@font-face {
    font-family: 'Noto Serif SC';
    src: url('data:font/truetype;base64,${NOTO_SERIF_SC_B64}') format('truetype');
  }`;
  document.head.appendChild(style);
}
```

**SplitLayout component (left-image right-text):**
```tsx
import { useCurrentFrame, useVideoConfig, spring, staticFile, Img } from "remotion";

const SplitLayout: React.FC<{ imageSrc: string; children: React.ReactNode }> = ({ imageSrc, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const imgOpacity = spring({ frame, fps, from: 0, to: 1, config: { damping: 20 } });
  const imgScale = spring({ frame, fps, from: 0.92, to: 1, config: { damping: 18 } });

  return (
    <div style={{ display: "flex", width: "100%", height: "100%", alignItems: "center", padding: "60px 80px", gap: 60 }}>
      <div style={{
        flex: "0 0 52%", opacity: imgOpacity, transform: `scale(${imgScale})`,
        background: "rgba(255,255,255,0.97)", borderRadius: 20, padding: 16,
        boxShadow: "0 0 40px rgba(100,180,255,0.35), 0 8px 32px rgba(0,0,0,0.4)",
        display: "flex", alignItems: "center", justifyContent: "center",
        maxHeight: "75%", overflow: "hidden",
      }}>
        <Img src={imageSrc} style={{ width: "100%", height: "auto", objectFit: "contain", borderRadius: 12 }} />
      </div>
      <div style={{ flex: 1, display: "flex", flexDirection: "column", justifyContent: "center" }}>
        {children}
      </div>
    </div>
  );
};
```

**Render command:**
```bash
cd /workspace/project

# Test frame first
npx remotion still BioDesignBench --frame=150 --output=/tmp/test.png \
  --browser-executable=$(which chromium)

# Full render
npx remotion render BioDesignBench \
  --concurrency=1 \
  --output=/workspace/output.mp4 \
  --browser-executable=$(which chromium)
```

### Step 7B — Render with HyperFrames

**Environment setup:**
```bash
# Node.js 22 required
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt-get install -y nodejs ffmpeg chromium

npm install -g hyperframes
# or: npx hyperframes@latest
```

**HyperFrames composition structure:**
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { width: 1920px; height: 1080px; overflow: hidden; background: #0a1628; }
    .clip { position: absolute; width: 1920px; height: 1080px; opacity: 0; }
  </style>
</head>
<body
  data-composition-id="main"
  data-width="1920"
  data-height="1080"
  data-fps="30"
  data-start="0"
  data-duration="141"
>
  <!-- Scene 0: Cover (0-5s = frames 0-150) -->
  <div class="clip" data-start="0" data-duration="5" data-track-index="0">
    <div style="display:flex; align-items:center; justify-content:center; height:100%; color:white; font-size:72px; font-family:'Noto Serif SC',serif;">
      AI能设计蛋白质，但它真的懂蛋白质吗？
    </div>
  </div>

  <!-- Scene 1: Background (5-25s = frames 150-750) -->
  <div class="clip" data-start="5" data-duration="20" data-track-index="0">
    <!-- content -->
  </div>
</body>
<script>
  // GSAP timeline registration (required by HyperFrames lint)
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });

  // Scene 0 animations
  tl.set(".clip[data-start='0']", { opacity: 1 }, 0)
    .from(".clip[data-start='0'] div", { opacity: 0, y: 30, duration: 0.8 }, 0.2)
    .set(".clip[data-start='0']", { opacity: 0 }, 5);  // hard-kill at scene end

  // Scene 1 animations
  tl.set(".clip[data-start='5']", { opacity: 1 }, 5)
    .from(".clip[data-start='5'] *", { opacity: 0, duration: 0.6, stagger: 0.1 }, 5.3)
    .set(".clip[data-start='5']", { opacity: 0 }, 25);

  window.__timelines["main"] = tl;
</script>
</html>
```

**HyperFrames render command:**
```bash
# Preview in browser
npx hyperframes preview --file composition.html

# Render to MP4 (silent)
npx hyperframes render --file composition.html --output /workspace/silent.mp4 --workers 4

# Add audio with ffmpeg
ffmpeg -y -i /workspace/silent.mp4 -i /workspace/audio_final.mp3 \
  -c:v copy -c:a aac -shortest /workspace/output.mp4
```

**HyperFrames lint rules (critical):**
- Root `<body>` must have: `data-composition-id`, `data-width`, `data-height`, `data-fps`, `data-start`, `data-duration`
- Scene divs use `class="clip"` (NOT `class="scene"`)
- Use `data-duration` (NOT `data-end`)
- Use `data-track-index` for layering
- GSAP timeline must be registered: `window.__timelines["composition-id"] = tl`
- Hard-kill opacity at scene end: `tl.set(el, {opacity:0}, end_time)` — required to prevent scene bleed
- No `Math.random()` — must be deterministic

### Step 7C — Render with Playwright (no Node.js)

```python
from playwright.sync_api import sync_playwright
import subprocess, os

def render_video_playwright(html_path: str, scenes: list, out_path: str,
                             fps: int = 30, width: int = 1920, height: int = 1080):
    """
    scenes: [{"start_frame": 0, "end_frame": 150, "html_content": "..."}, ...]
    """
    frames_dir = "/workspace/frames"
    os.makedirs(frames_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(f"file://{html_path}")

        frame_num = 0
        for scene in scenes:
            for f in range(scene["start_frame"], scene["end_frame"]):
                # Update scene state
                page.evaluate(f"window.setFrame({f})")
                page.screenshot(path=f"{frames_dir}/frame_{frame_num:06d}.png")
                frame_num += 1

        browser.close()

    # Encode with ffmpeg
    subprocess.run([
        "ffmpeg", "-y", "-framerate", str(fps),
        "-i", f"{frames_dir}/frame_%06d.png",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        out_path
    ], check=True)
```

### Step 8 — Process Logo

```python
from PIL import Image
import numpy as np

def make_white_logo(logo_path: str, out_path: str):
    """Convert black-on-white logo to white-on-transparent"""
    img = Image.open(logo_path).convert("RGBA")
    arr = np.array(img)
    r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
    brightness = (r.astype(int) + g.astype(int) + b.astype(int)) / 3
    new_arr = np.zeros_like(arr)
    new_arr[:,:,0] = 255  # white
    new_arr[:,:,1] = 255
    new_arr[:,:,2] = 255
    new_arr[:,:,3] = (255 - brightness).astype(np.uint8)
    Image.fromarray(new_arr).save(out_path)
```

**BioTenderLogo Remotion component:**
```tsx
// src/BioTenderLogo.tsx
import { Img, staticFile } from "remotion";

export const BioTenderLogo: React.FC<{ size?: number }> = ({ size = 80 }) => (
  <div style={{
    position: "absolute", bottom: 32, right: 40,
    opacity: 0.85, zIndex: 100,
  }}>
    <Img src={staticFile("images/logo_white.png")}
         style={{ width: size, height: "auto" }} />
  </div>
);
```

### Step 9 — Quality Verification

```bash
# Extract frames at key timestamps
ffmpeg -ss 4   -i output.mp4 -frames:v 1 /tmp/check_cover.png -y
ffmpeg -ss 20  -i output.mp4 -frames:v 1 /tmp/check_sc1.png -y
ffmpeg -ss 70  -i output.mp4 -frames:v 1 /tmp/check_mid.png -y
ffmpeg -ss 135 -i output.mp4 -frames:v 1 /tmp/check_outro.png -y
```

Check with `Read(mode="low")`:
- Chinese characters render without tofu boxes
- BioTender watermark visible bottom-right
- Left-image right-text layout: paper figure visible in left panel
- Animations smooth (no frozen frames)
- Audio present (file size > 5 MB for ~2min video)
- Subtitles visible and synced (if enabled)

```bash
# Copy to results
cp /workspace/output.mp4 /mnt/results/<paper_name>_video.mp4
```

---

## Vertical Video (1080×1920) Adaptation

For short-form platforms (TikTok, Reels, Shorts):

```python
# Adjust scene layout for vertical
VERTICAL_STYLE = {
    "width": 1080,
    "height": 1920,
    "title_font_size": 56,
    "body_font_size": 36,
    "padding": "80px 60px",
}

# Remotion composition
# <Composition width={1080} height={1920} ...>

# HyperFrames body
# data-width="1080" data-height="1920"
```

**Vertical layout tips:**
- Stack image above text (not side-by-side)
- Larger font sizes (56px title, 36px body)
- Shorter scenes (8–15s each)
- Total length: 60–90s for Reels/Shorts

---

## Bilingual Video (Chinese + English Subtitles)

```python
# Generate both Chinese TTS and English subtitles
async def gen_bilingual(zh_scripts: dict, en_scripts: dict, out_dir: str):
    # Chinese TTS (narration)
    for key, text in zh_scripts.items():
        comm = edge_tts.Communicate(text, "zh-CN-XiaoxiaoNeural", rate="-5%")
        await comm.save(f"{out_dir}/{key}_zh.mp3")
    # English TTS (optional, for EN version)
    for key, text in en_scripts.items():
        comm = edge_tts.Communicate(text, "en-US-JennyNeural", rate="-5%")
        await comm.save(f"{out_dir}/{key}_en.mp3")
```

**Burn bilingual subtitles:**
```bash
# Chinese subtitles (bottom)
ffmpeg -y -i output.mp4 \
  -vf "subtitles=zh_subs.ass:fontsdir=/usr/share/fonts" \
  -c:a copy output_zh_sub.mp4

# English subtitles (bottom, different style)
ffmpeg -y -i output.mp4 \
  -vf "subtitles=en_subs.ass:fontsdir=/usr/share/fonts" \
  -c:a copy output_en_sub.mp4
```

---

## Scientific Caveats

- **Scores shown in leaderboard scenes must be verified** against paper tables/figures. Always use exact values from the paper, not approximations.
- **TTS narration is AI-generated** — verify technical terms are pronounced correctly (e.g., "RFdiffusion", "ProteinMPNN").
- **Font rendering**: Noto Serif CJK SC covers Simplified Chinese. For Traditional Chinese, use `NotoSerifCJK-TC`. For Japanese/Korean, use respective variants.
- **BGM copyright**: User-provided MP3 may have copyright restrictions. Programmatically synthesized BGM (Am-F-C-G pad) is copyright-free.
- **Figure extraction**: PyMuPDF extracts raster images embedded in PDF. Vector figures (SVG/PDF-native) may not be extracted. Use `min_width=400, min_height=300` to filter out icons and logos.
- **F5-TTS voice cloning**: Requires user consent for reference voice. Do not clone voices without permission.
- **edge-tts rate limits**: Microsoft's TTS service may throttle heavy usage. Add `asyncio.sleep(0.5)` between requests if needed.

---

## Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `registerRoot not found` | `src/index.ts` must call `registerRoot(RemotionRoot)` |
| Chinese tofu boxes | Install `fonts-noto-cjk` via apt; use `loadFonts()` with `staticFile()` paths; or embed fonts as base64 |
| Emoji boxes | Replace all emoji with unicode geometric symbols (◈ ◉ ◆ ◎ ▶ ✓ ✗) |
| Audio silent after 2:00 (TTS) | Never concatenate all TTS into one global audio track — use per-scene `<Audio src={staticFile("audio/scX.mp3")} />` inside each Scene component |
| Audio silent after 2:00 (BGM) | `duration=first` truncates BGM to TTS length; use `apad=whole_dur=VIDEO_DUR` + `duration=longest` |
| Audio not synced | TTS: per-scene `<Audio>` in each Scene component. BGM: single global `<Audio>` in Root pointing to BGM-only track |
| `asyncio.run()` error in Jupyter | Add `import nest_asyncio; nest_asyncio.apply()` before async calls |
| Font CDN fails in headless | Copy font files to `public/fonts/`, serve via `staticFile()` |
| Figure not showing in SplitLayout | Ensure image is in `public/images/paper/` and referenced via `staticFile()` |
| PyMuPDF extracts wrong images | Increase `min_width`/`min_height` thresholds; inspect extracted files manually |
| HyperFrames: scene bleeds into next | Add hard-kill: `tl.set(el, {opacity:0}, end_time)` after each scene exit |
| HyperFrames: lint error on `data-end` | Use `data-duration` (seconds), not `data-end` |
| HyperFrames: `__timelines` not found | Register: `window.__timelines["composition-id"] = tl` |
| HyperFrames: Node.js version error | Requires Node.js 22+; Remotion works with Node.js 20+ |
| F5-TTS "核嗓" (voice break) | Split long text into <150 char segments; increase `nfe_step` to 32 |
| F5-TTS very slow on CPU | RTF≈18x is expected; use GPU or switch to edge-tts for speed |
| CosyVoice2 import error | Install: `pip install cosyvoice`; check CUDA version compatibility |
| Remotion render to /mnt/results/ fails | Render to `/workspace/` first, then `cp` to `/mnt/results/` (S3 doesn't support random-access writes) |
| Playwright frame capture slow | Use `--workers 4` in HyperFrames; or use Remotion with `--concurrency=4` on multi-core machine |
| Font subset too large | Use `pyftsubset` to subset to only characters used in scripts |

---

## Example Trigger Prompts

**Chinese:**
- "看一下这篇PDF，然后渲染成视频，用edge tts的中文普通话女声"
- "把这篇论文做成科普视频，加上BioTender水印"
- "这篇bioRxiv文章能做成短视频吗？"
- "放一些文章图片在视频里面，可以做成左图右字"
- "用晓伊的声音做一个2分钟的视频"
- "做成竖版视频，适合发抖音"
- "加上中文字幕"
- "用我的声音克隆做旁白" (triggers F5-TTS/CosyVoice2)
- "做成双语版，中文旁白+英文字幕"

**English:**
- "Convert this paper to a 2-minute explainer video in Chinese"
- "Make a science video from this PDF with English narration"
- "Render this HTML article as a video with Jenny's voice"
- "Create a vertical video for Instagram Reels"
- "Add subtitles to the video"
- "Use voice cloning with my reference audio"

---

## Session History & Proven Configurations

The following configurations have been tested and verified in production:

| Video | Engine | TTS | Duration | Notes |
|-------|--------|-----|----------|-------|
| BioDesignBench v2 | Remotion 4.0.290 | XiaoxiaoNeural -5% | 141s | Left-image right-text, 4 paper figures |
| Genie 3 v3 | HyperFrames 0.5.5 | XiaoxiaoNeural -5% | 204s | ASS subtitles, 4 HTML figures |
| Isomorphic Labs B轮 | Remotion 4.0.460 | XiaoxiaoNeural +5% | 68.7s | Source Han Sans, 8 scenes |
| Physical AI Wet Lab v4 | Remotion 4.x | XiaoxiaoNeural | 127s | Base64 font embed, 9 scenes |
| BioTender Physical AI v3 | Remotion 4.0.460 | XiaoxiaoNeural | 169.9s | 2 HTML images, 10 scenes |
| Click.mAb. v5 | HyperFrames 0.5.5 | F5-TTS (voice clone) | 80.4s | CPU voice cloning |
| 倒反天罡 v2 | Playwright | XiaoxiaoNeural | 112.5s | No Node.js, SRT subtitles |
| blatant-why bilingual | Remotion 4.0.460 | en-US-JennyNeural | 233s | EN narration + ZH/EN subs |
