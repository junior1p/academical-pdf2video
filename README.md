# academical-pdf2video

> Convert academic PDF papers into polished narrated videos using AI + Remotion

## Overview

**academical-pdf2video** is an AI-powered pipeline that transforms any scientific PDF paper into a 1920×1080 MP4 video with:

- 🎙️ Chinese TTS narration (`edge-tts` zh-CN-XiaoxiaoNeural)
- 🎵 Background music (user-provided MP3 or auto-synthesized Am-F-C-G pad)
- 🖼️ Optional paper figure embeds (left-image right-text layout)
- 💧 BioTender logo watermark
- ✨ Smooth animations via [Remotion](https://www.remotion.dev/) (React/TypeScript)

## Features

| Feature | Details |
|---------|---------|
| Video resolution | 1920×1080, 30fps, H.264+AAC |
| TTS engine | `edge-tts` — `zh-CN-XiaoxiaoNeural` (default) |
| Video lengths | Concise (~2min) / Standard (~4min) / Detailed (~6min) |
| Figure embedding | PyMuPDF extraction + SplitLayout component |
| BGM | User MP3 or programmatic Am-F-C-G synthesis |
| Font | Noto Serif CJK SC (headless Chrome safe) |

## Workflow

```
PDF → Read & Summarize → Write Scene Scripts → TTS Audio → Mix BGM
    → Build Remotion Project → Render → Quality Verification → MP4
```

See [SKILL.md](./SKILL.md) for the complete step-by-step implementation guide.

## Quick Start

### Prerequisites

```bash
# Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs ffmpeg chromium fonts-noto-cjk

# Python packages
pip install edge-tts pymupdf pillow numpy scipy nest_asyncio

# Remotion
npm install --save-exact remotion@4.0.290 @remotion/cli@4.0.290 @remotion/renderer@4.0.290 react@18.3.1 react-dom@18.3.1
```

### Usage

```python
# 1. Extract and summarize PDF
# 2. Generate TTS audio per scene
# 3. Build Remotion project with scene components
# 4. Render to MP4

npx remotion render BioDesignBench \
  --concurrency=1 \
  --output=output.mp4 \
  --browser-executable=$(which chromium)
```

## Example Trigger Prompts

- "看一下这篇PDF，然后渲染成视频，用edge tts的中文普通话女声"
- "把这篇论文做成科普视频，加上BioTender水印"
- "Convert this paper to a 2-minute explainer video in Chinese"
- "放一些文章图片在视频里面，可以做成左图右字"

## Architecture

```
Root.tsx   ←  Global BGM track (bgm_mixed.mp3)
  └── Scene0  ←  TTS audio (sc0.mp3) + animations
  └── Scene1  ←  TTS audio (sc1.mp3) + SplitLayout (paper figure)
  └── ...
  └── Scene7  ←  TTS audio (sc7.mp3) + outro
```

**Key design decision**: Per-scene TTS audio (not concatenated global track) ensures audio stays perfectly synced even with per-scene buffer frames.

## Credits

Built by [BioTender](https://github.com/junior1p) · Powered by Remotion + edge-tts + PyMuPDF
