<div align="center">

<img src="https://raw.githubusercontent.com/junior1p/sci2video/main/assets/banner.png" alt="sci2video banner" width="100%" />

# sci2video

**Convert academic PDF papers and HTML articles into polished, narrated science videos using AI**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)
[![Remotion](https://img.shields.io/badge/Remotion-4.0.290-E14D2A?style=flat-square&logo=react)](https://www.remotion.dev/)
[![HyperFrames](https://img.shields.io/badge/HyperFrames-0.5.5-22C55E?style=flat-square)](https://github.com/heygen-com/hyperframes)
[![edge-tts](https://img.shields.io/badge/edge--tts-7.x-0078D4?style=flat-square&logo=microsoft)](https://github.com/rany2/edge-tts)
[![Examples](https://img.shields.io/badge/Examples-v1.0.0%20Release-F59E0B?style=flat-square&logo=github)](https://github.com/junior1p/sci2video/releases/tag/v1.0.0)

<br/>

[Overview](#overview) · [Quick Start](#quick-start) · [TTS Engines](#tts-engines) · [Rendering Backends](#rendering-backends) · [Examples](#example-videos) · [Documentation](#documentation)

</div>

---

## Overview

**sci2video** is a production-ready pipeline that transforms any scientific PDF or HTML article into a broadcast-quality MP4 video. Built by [BioTender](https://github.com/junior1p) and battle-tested across 50+ real science communication videos.

```
PDF / HTML  ──►  AI Summarization  ──►  TTS Narration  ──►  Video Rendering  ──►  MP4
```

### What it produces

| Output | Spec |
|--------|------|
| Resolution | 1920 × 1080 (landscape) or 1080 × 1920 (vertical) |
| Frame rate | 30 fps |
| Codec | H.264 + AAC |
| Typical length | 1–6 minutes |
| Languages | 74 languages, 322 voices |

---

## Quick Start

### Prerequisites

```bash
# System dependencies
apt-get install -y ffmpeg chromium fonts-noto-cjk

# Node.js 20+ (for Remotion) or 22+ (for HyperFrames)
curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && apt-get install -y nodejs

# Python packages
pip install edge-tts pymupdf pillow numpy scipy nest_asyncio beautifulsoup4

# Remotion
npm install --save-exact remotion@4.0.290 @remotion/cli@4.0.290 @remotion/renderer@4.0.290 \
  react@18.3.1 react-dom@18.3.1

# HyperFrames
npm install -g hyperframes
```

### Minimal example

```python
import asyncio, edge_tts, nest_asyncio
nest_asyncio.apply()

scripts = {
    "sc0": "",                                          # title card
    "sc1": "这篇论文来自斯坦福大学，研究了大语言模型在蛋白质设计中的应用。",
    "sc2": "研究团队构建了包含76个任务的基准测试，覆盖从头设计到功能预测的全流程。",
    "sc3": "测试结果显示，通过简单的提示词干预，GPT-5的得分提升了15.9分。",
    "sc4": "这不是能力瓶颈，而是行为瓶颈。AI蛋白质设计的下一步，在于对齐。",
}

async def gen():
    for key, text in scripts.items():
        if text:
            await edge_tts.Communicate(text, "zh-CN-XiaoxiaoNeural", rate="-5%").save(f"{key}.mp3")

asyncio.get_event_loop().run_until_complete(gen())
```

See [`examples/quickstart.py`](./examples/quickstart.py) for the full runnable script.

---

## TTS Engines

Choose the engine that fits your use case:

| Engine | Languages | Voice Cloning | Speed | GPU Required | License |
|--------|-----------|:-------------:|-------|:------------:|---------|
| **edge-tts** | 74 langs · 322 voices | — | ⚡ Very fast | No | Free |
| **F5-TTS** | ZH + EN | ✓ 5 s sample | 🐢 Slow on CPU | Optional | MIT |
| **CosyVoice 2** | 9 langs + 18 dialects | ✓ Zero-shot | ⚡ Fast | Recommended | Apache 2.0 |
| **Kokoro** | 9 languages | — | ⚡ Very fast | No | Apache 2.0 |
| **GPT-SoVITS** | ZH / EN / JP / KR / Cantonese | ✓ 5 s sample | 🔶 Medium | Recommended | MIT |

### Recommended voices

```python
VOICES = {
    # Chinese
    "zh_science":   ("zh-CN-XiaoxiaoNeural",  "-5%"),   # warm female — default
    "zh_news":      ("zh-CN-YunyangNeural",   "+0%"),   # male news anchor
    "zh_energetic": ("zh-CN-YunxiNeural",     "+5%"),   # male, tech/startup
    # English
    "en_science":   ("en-US-JennyNeural",     "-5%"),   # friendly female — default
    "en_formal":    ("en-US-GuyNeural",       "+0%"),   # natural male
    # Japanese / Korean
    "ja":           ("ja-JP-NanamiNeural",    "+0%"),
    "ko":           ("ko-KR-SunHiNeural",     "+0%"),
}
```

Full voice reference → [`docs/voices.md`](./docs/voices.md)

---

## Rendering Backends

| Backend | Authoring | License | Node.js | Best For |
|---------|-----------|---------|:-------:|----------|
| **Remotion** | React / TSX | Source-available (free < 3 seats) | 20+ | Data-driven scenes, charts, reusable components |
| **HyperFrames** | HTML + GSAP | Apache 2.0 | 22+ | Kinetic typography, HTML articles, AI-generated compositions |
| **Playwright** | HTML + CSS | Apache 2.0 | — | Simple slides, environments without Node.js |

### Audio architecture (critical for sync)

```
Root.tsx
  ├── <Audio src="bgm_mixed.mp3" />        ← global BGM track only
  ├── Scene 0  <Audio src="sc0.mp3" />     ← per-scene TTS fires on scene start
  ├── Scene 1  <Audio src="sc1.mp3" />
  └── Scene N  <Audio src="scN.mp3" />
```

> **Why per-scene audio?** Each scene has a 2.5 s buffer after TTS ends. Concatenating all TTS into one global track causes cumulative offset drift — later scenes' narration plays before those scenes appear on screen. Per-scene audio eliminates this entirely.

---

## Example Videos

All examples are available in the [**v1.0.0 Release**](https://github.com/junior1p/sci2video/releases/tag/v1.0.0).

### Chinese Narration · edge-tts `zh-CN-XiaoxiaoNeural`

| Video | Description | Backend | Duration |
|-------|-------------|---------|:--------:|
| [BioDesignBench v2](https://github.com/junior1p/sci2video/releases/download/v1.0.0/biodesignbench_video_v2.mp4) | BioDesignBench 论文 · 左图右字 · 4 张论文原图嵌入 | Remotion | 141 s |
| [Genie 3 v3](https://github.com/junior1p/sci2video/releases/download/v1.0.0/genie3_video_v3.mp4) | Genie 3 文章 · HyperFrames · ASS 字幕 | HyperFrames | 204 s |
| [Physical AI Wet Lab](https://github.com/junior1p/sci2video/releases/download/v1.0.0/physical_ai_wetlab_v4.mp4) | Physical AI 湿实验室 · base64 字体嵌入 · 9 场景 | Remotion | 127 s |
| [Isomorphic Labs B 轮](https://github.com/junior1p/sci2video/releases/download/v1.0.0/isomorphic_labs_series_b_v2.mp4) | 融资公告 · 思源黑体 · 8 场景 | Remotion | 69 s |
| [倒反天罡 v2](https://github.com/junior1p/sci2video/releases/download/v1.0.0/daofantiangang_v2.mp4) | 药企资产被 AI 公司收购 · Playwright · SRT 字幕 | Playwright | 113 s |

### English Narration · edge-tts `en-US-JennyNeural`

| Video | Description | Backend | Duration |
|-------|-------------|---------|:--------:|
| [AI Protein Design Review](https://github.com/junior1p/sci2video/releases/download/v1.0.0/ai_protein_design_review_en.mp4) | AI 蛋白质设计综述 · 全英文旁白 + 英文字幕 | HyperFrames | 161 s |
| [24 h AI Drug Discovery](https://github.com/junior1p/sci2video/releases/download/v1.0.0/24h_ai_drug_en.mp4) | 24 小时 AI 药物发现 · 英文旁白 | HyperFrames | 90 s |

### Voice Cloning · F5-TTS

| Video | Description | Backend | Duration |
|-------|-------------|---------|:--------:|
| [Click.mAb.](https://github.com/junior1p/sci2video/releases/download/v1.0.0/clickmab_f5tts_voice_clone.mp4) | 科迈生物 Click.mAb. 产品评测 · F5-TTS 语音克隆 | HyperFrames | 80 s |

### Vertical Video · 1080 × 1920

| Video | Description | Backend | Duration |
|-------|-------------|---------|:--------:|
| [BioTender Scholar Program](https://github.com/junior1p/sci2video/releases/download/v1.0.0/biotender_scholar_vertical_1080x1920.mp4) | BioTender 学者计划 · 竖版 · 适合抖音 / Reels / Shorts | HyperFrames | 90 s |

### Bilingual · EN narration + ZH subtitles

| Video | Description | Backend | Duration |
|-------|-------------|---------|:--------:|
| [blatant-why](https://github.com/junior1p/sci2video/releases/download/v1.0.0/blatant_why_en_narration_zh_subtitles.mp4) | 蛋白质设计工具介绍 · 英文旁白 + 中文字幕 | Remotion | 233 s |

---

## Documentation

| File | Description |
|------|-------------|
| [`SKILL.md`](./SKILL.md) | Complete implementation guide — all steps, code templates, error fixes |
| [`docs/voices.md`](./docs/voices.md) | Full TTS voice reference — 322 edge-tts voices + voice cloning engines |
| [`examples/quickstart.py`](./examples/quickstart.py) | Runnable quick-start script |

---

## Proven Configurations

Configurations verified in production across 50+ videos:

| Video | Backend | TTS Engine | Duration | Notes |
|-------|---------|------------|:--------:|-------|
| BioDesignBench v2 | Remotion 4.0.290 | XiaoxiaoNeural −5% | 141 s | 4 paper figures, SplitLayout |
| Genie 3 v3 | HyperFrames 0.5.5 | XiaoxiaoNeural −5% | 204 s | ASS subtitles, 4 HTML figures |
| Isomorphic Labs B 轮 | Remotion 4.0.460 | XiaoxiaoNeural +5% | 69 s | Source Han Sans, 8 scenes |
| Physical AI Wet Lab v4 | Remotion 4.x | XiaoxiaoNeural | 127 s | Base64 font embed, 9 scenes |
| BioTender Physical AI v3 | Remotion 4.0.460 | XiaoxiaoNeural | 170 s | 2 HTML images, 10 scenes |
| Click.mAb. v5 | HyperFrames 0.5.5 | F5-TTS (voice clone) | 80 s | CPU voice cloning |
| 倒反天罡 v2 | Playwright | XiaoxiaoNeural | 113 s | No Node.js, SRT subtitles |
| blatant-why bilingual | Remotion 4.0.460 | JennyNeural (EN) | 233 s | EN narration + ZH/EN subs |

---

## Trigger Prompts

The pipeline activates on prompts like:

```
"看一下这篇PDF，然后渲染成视频，用edge tts的中文普通话女声"
"把这篇论文做成科普视频，加上BioTender水印"
"放一些文章图片在视频里面，可以做成左图右字"
"用我的声音克隆做旁白"
"做成竖版视频，适合发抖音"
"Convert this paper to a 2-minute explainer video in Chinese"
"Make a science video with English narration and Chinese subtitles"
"Create a vertical video for Instagram Reels"
```

---

<div align="center">

Built by [BioTender](https://github.com/junior1p) &nbsp;·&nbsp;
Powered by [Remotion](https://www.remotion.dev/) + [HyperFrames](https://github.com/heygen-com/hyperframes) + [edge-tts](https://github.com/rany2/edge-tts) + [F5-TTS](https://github.com/SWivid/F5-TTS) + [CosyVoice](https://github.com/FunAudioLLM/CosyVoice) + [PyMuPDF](https://pymupdf.readthedocs.io/)

</div>
