# academical-pdf2video

> Convert academic PDF papers or HTML articles into polished narrated videos using AI + Remotion / HyperFrames

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

## Overview

**academical-pdf2video** is an AI-powered pipeline that transforms any scientific PDF or HTML article into a 1920×1080 (or 1080×1920 vertical) MP4 video with:

- Multiple TTS engines: edge-tts, F5-TTS voice cloning, CosyVoice2, Kokoro
- Multiple rendering backends: Remotion (React/TSX) or HyperFrames (HTML/GSAP)
- Bilingual support: Chinese narration + English subtitles (or vice versa)
- Optional paper figure embeds (left-image right-text layout)
- BioTender logo watermark
- ASS/SRT subtitle burn-in
- Vertical video (1080×1920) for TikTok / Reels / Shorts

## TTS Engine Comparison

| Engine | Languages | Voice Cloning | Speed | Best For |
|--------|-----------|---------------|-------|----------|
| **edge-tts** | 74 langs, 322 voices | No | Very fast | Quick, reliable, no GPU |
| **F5-TTS** | ZH + EN | Yes (5s sample) | Slow on CPU | Custom voice cloning |
| **CosyVoice2** | 9 langs + 18 dialects | Yes | Fast (GPU) | Emotion/dialect control |
| **Kokoro** | 9 languages | No | Very fast | Lightweight, no GPU |
| **GPT-SoVITS** | ZH/EN/JP/KR/Cantonese | Yes (5s) | Medium | Highest quality cloning |

## Rendering Backend Comparison

| Backend | Authoring | License | Node.js | Best For |
|---------|-----------|---------|---------|----------|
| **Remotion** | React/TSX | Source-available | 20+ | Data-driven scenes, charts |
| **HyperFrames** | HTML+GSAP | Apache 2.0 | 22+ | Kinetic typography, HTML articles |
| **Playwright** | HTML+CSS | Apache 2.0 | Not needed | Simple slides, no Node.js |

## Key Features

| Feature | Details |
|---------|---------|
| Video resolution | 1920×1080 or 1080×1920, 30fps, H.264+AAC |
| TTS engines | edge-tts / F5-TTS / CosyVoice2 / Kokoro |
| Video lengths | Concise (~2min) / Standard (~4min) / Detailed (~6min) |
| Figure embedding | PyMuPDF extraction + SplitLayout component |
| BGM | User MP3 or programmatic Am-F-C-G synthesis |
| Subtitles | ASS/SRT burn-in via ffmpeg |
| Languages | Chinese (ZH-CN/HK/TW), English, Japanese, Korean, + 70 more |
| Orientation | Landscape 1920×1080 or Vertical 1080×1920 |

## Workflow

```
Source (PDF/HTML)
  → Read & Summarize
  → Extract Figures (optional)
  → Write Scene Scripts
  → Generate TTS Audio (edge-tts / F5-TTS / CosyVoice2 / Kokoro)
  → Mix BGM
  → Build Subtitle Track (optional)
  → Render (Remotion / HyperFrames / Playwright)
  → Quality Verification
  → MP4
```

See [SKILL.md](./SKILL.md) for the complete step-by-step implementation guide with all code templates.

## Quick Start

### Prerequisites

```bash
# System dependencies
apt-get install -y nodejs ffmpeg chromium fonts-noto-cjk

# Python packages
pip install edge-tts pymupdf pillow numpy scipy nest_asyncio beautifulsoup4

# Remotion (Node.js 20+)
npm install --save-exact remotion@4.0.290 @remotion/cli@4.0.290 @remotion/renderer@4.0.290 react@18.3.1 react-dom@18.3.1

# HyperFrames (Node.js 22+)
npm install -g hyperframes
```

### Usage Examples

```bash
# edge-tts: Chinese female voice (default)
python gen_tts.py --voice zh-CN-XiaoxiaoNeural --rate "-5%"

# edge-tts: English female voice
python gen_tts.py --voice en-US-JennyNeural --rate "-5%"

# F5-TTS: voice cloning
f5-tts_infer-cli --ref_audio reference.wav --gen_text "..." --output sc1.wav

# Remotion render
npx remotion render BioDesignBench --concurrency=1 --output=output.mp4

# HyperFrames render
npx hyperframes render --file composition.html --output output.mp4 --workers 4
```

## Audio Architecture (Critical)

```
Root.tsx   ←  Global BGM track (bgm_mixed.mp3)
  └── Scene0  ←  Per-scene TTS (sc0.mp3) + animations
  └── Scene1  ←  Per-scene TTS (sc1.mp3) + SplitLayout (paper figure)
  └── ...
  └── SceneN  ←  Per-scene TTS (scN.mp3) + outro
```

**Key design decision**: Per-scene TTS audio (not concatenated global track) ensures audio stays perfectly synced even with per-scene buffer frames.

## Proven Configurations

| Video | Engine | TTS | Duration |
|-------|--------|-----|----------|
| BioDesignBench v2 | Remotion 4.0.290 | XiaoxiaoNeural | 141s |
| Genie 3 v3 | HyperFrames 0.5.5 | XiaoxiaoNeural | 204s |
| Isomorphic Labs B轮 | Remotion 4.0.460 | XiaoxiaoNeural | 68.7s |
| Physical AI Wet Lab | Remotion 4.x | XiaoxiaoNeural | 127s |
| Click.mAb. v5 | HyperFrames 0.5.5 | F5-TTS (clone) | 80.4s |
| 倒反天罡 v2 | Playwright | XiaoxiaoNeural | 112.5s |
| blatant-why bilingual | Remotion 4.0.460 | JennyNeural (EN) | 233s |

## Example Trigger Prompts

**Chinese:**
- "看一下这篇PDF，然后渲染成视频，用edge tts的中文普通话女声"
- "把这篇论文做成科普视频，加上BioTender水印"
- "放一些文章图片在视频里面，可以做成左图右字"
- "用我的声音克隆做旁白"
- "做成竖版视频，适合发抖音"
- "加上中文字幕"

**English:**
- "Convert this paper to a 2-minute explainer video in Chinese"
- "Make a science video with English narration and Chinese subtitles"
- "Create a vertical video for Instagram Reels"
- "Use voice cloning with my reference audio"

## Credits

Built by [BioTender](https://github.com/junior1p) · Powered by Remotion + HyperFrames + edge-tts + F5-TTS + CosyVoice2 + PyMuPDF
