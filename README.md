# academical-pdf2video

> Convert academic PDF papers or HTML articles into polished narrated videos using AI + Remotion / HyperFrames

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Examples](https://img.shields.io/badge/Examples-v1.0.0-green)](https://github.com/junior1p/academical-pdf2video/releases/tag/v1.0.0)

## Overview

**academical-pdf2video** is an AI-powered pipeline that transforms any scientific PDF or HTML article into a 1920×1080 (or 1080×1920 vertical) MP4 video with:

- Multiple TTS engines: edge-tts, F5-TTS voice cloning, CosyVoice2, Kokoro
- Multiple rendering backends: Remotion (React/TSX) or HyperFrames (HTML/GSAP)
- Bilingual support: Chinese narration + English subtitles (or vice versa)
- Optional paper figure embeds (left-image right-text layout)
- BioTender logo watermark
- ASS/SRT subtitle burn-in
- Vertical video (1080×1920) for TikTok / Reels / Shorts

---

## Example Videos

All examples are available in the [v1.0.0 Release](https://github.com/junior1p/academical-pdf2video/releases/tag/v1.0.0).

### Chinese Narration (edge-tts `zh-CN-XiaoxiaoNeural`)

| Video | Description | Engine | Duration | Download |
|-------|-------------|--------|----------|----------|
| BioDesignBench v2 | BioDesignBench论文，左图右字，4张论文原图嵌入 | Remotion | 141s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/biodesignbench_video_v2.mp4) |
| Genie 3 v3 | Genie 3文章，HyperFrames渲染，ASS字幕 | HyperFrames | 204s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/genie3_video_v3.mp4) |
| Physical AI Wet Lab | Physical AI Wet Lab，base64字体嵌入，9场景 | Remotion | 127s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/physical_ai_wetlab_v4.mp4) |
| Isomorphic Labs B轮 | Isomorphic Labs融资公告，思源黑体，8场景 | Remotion | 69s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/isomorphic_labs_series_b_v2.mp4) |
| 倒反天罡 v2 | 药企资产被AI公司收购，Playwright渲染，SRT字幕 | Playwright | 113s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/daofantiangang_v2.mp4) |

### English Narration (edge-tts `en-US-JennyNeural`)

| Video | Description | Engine | Duration | Download |
|-------|-------------|--------|----------|----------|
| AI Protein Design Review | AI蛋白质设计综述，全英文旁白+英文字幕 | HyperFrames | 161s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/ai_protein_design_review_en.mp4) |
| 24h AI Drug Discovery | 24小时AI药物发现，英文旁白 | HyperFrames | 90s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/24h_ai_drug_en.mp4) |

### Voice Cloning (F5-TTS)

| Video | Description | Engine | Duration | Download |
|-------|-------------|--------|----------|----------|
| Click.mAb. | 科迈生物Click.mAb.产品评测，F5-TTS语音克隆旁白 | HyperFrames | 80s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/clickmab_f5tts_voice_clone.mp4) |

### Vertical Video (1080×1920)

| Video | Description | Engine | Duration | Download |
|-------|-------------|--------|----------|----------|
| BioTender Scholar Program | BioTender学者计划，竖版，适合抖音/Reels/Shorts | HyperFrames | 90s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/biotender_scholar_vertical_1080x1920.mp4) |

### Bilingual (EN narration + ZH subtitles)

| Video | Description | Engine | Duration | Download |
|-------|-------------|--------|----------|----------|
| blatant-why | 英文旁白+中文字幕，蛋白质设计工具介绍 | Remotion | 233s | [↓](https://github.com/junior1p/academical-pdf2video/releases/download/v1.0.0/blatant_why_en_narration_zh_subtitles.mp4) |

---

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
See [docs/voices.md](./docs/voices.md) for the full TTS voice reference (322 voices across 74 languages).

## Quick Start

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

## Audio Architecture (Critical)

```
Root.tsx   ←  Global BGM track (bgm_mixed.mp3)
  └── Scene0  ←  Per-scene TTS (sc0.mp3) + animations
  └── Scene1  ←  Per-scene TTS (sc1.mp3) + SplitLayout (paper figure)
  └── ...
  └── SceneN  ←  Per-scene TTS (scN.mp3) + outro
```

**Key design decision**: Per-scene TTS audio (not concatenated global track) ensures audio stays perfectly synced even with per-scene buffer frames.

## Credits

Built by [BioTender](https://github.com/junior1p) · Powered by Remotion + HyperFrames + edge-tts + F5-TTS + CosyVoice2 + PyMuPDF
