# TTS Voice Reference

Complete voice reference for the academical-pdf2video pipeline.

## edge-tts — Chinese Voices (zh-CN)

| Voice ID | 名字 | 性别 | 风格 | 适合场景 |
|----------|------|------|------|---------|
| `zh-CN-XiaoxiaoNeural` | 晓晓 | 女 | 温柔自然 | 科普视频（默认推荐） |
| `zh-CN-XiaoyiNeural` | 晓伊 | 女 | 甜美活泼 | 青少年内容 |
| `zh-CN-XiaohanNeural` | 晓涵 | 女 | 优雅知性 | 学术/纪录片 |
| `zh-CN-XiaochenNeural` | 晓辰 | 女 | 知性干练 | 研究论文 |
| `zh-CN-XiaomengNeural` | 晓梦 | 女 | 梦幻柔和 | 创意内容 |
| `zh-CN-XiaoruiNeural` | 晓睿 | 女 | 成熟权威 | 正式场合 |
| `zh-CN-XiaoshuangNeural` | 晓双 | 女 | 童声 | 教育内容 |
| `zh-CN-XiaomoNeural` | 晓墨 | 女 | 沉稳 | 商务内容 |
| `zh-CN-XiaoqiuNeural` | 晓秋 | 女 | 成熟 | 有声书 |
| `zh-CN-XiaorouNeural` | 晓柔 | 女 | 温柔 | 情感内容 |
| `zh-CN-YunxiNeural` | 云希 | 男 | 活力阳光 | 科技/创业 |
| `zh-CN-YunyangNeural` | 云扬 | 男 | 新闻播音 | 正式/新闻 |
| `zh-CN-YunjianNeural` | 云健 | 男 | 运动激情 | 动态内容 |
| `zh-CN-YunxiaNeural` | 云夏 | 男 | 年轻随性 | 轻松科普 |
| `zh-CN-YunfengNeural` | 云枫 | 男 | 成熟稳重 | 商务/纪录片 |
| `zh-CN-YunhaoNeural` | 云皓 | 男 | 活泼 | 娱乐内容 |

## edge-tts — Chinese Regional Dialects

| Voice ID | 方言 | 性别 |
|----------|------|------|
| `zh-CN-liaoning-XiaobeiNeural` | 辽宁话 | 女 |
| `zh-CN-shaanxi-XiaoniNeural` | 陕西话 | 女 |
| `zh-HK-HiuGaaiNeural` | 粤语 | 女 |
| `zh-HK-HiuMaanNeural` | 粤语 | 女 |
| `zh-HK-WanLungNeural` | 粤语 | 男 |
| `zh-TW-HsiaoChenNeural` | 台湾普通话 | 女 |
| `zh-TW-HsiaoYuNeural` | 台湾普通话 | 女 |
| `zh-TW-YunJheNeural` | 台湾普通话 | 男 |

## edge-tts — English Voices

| Voice ID | Style | Best For |
|----------|-------|----------|
| `en-US-JennyNeural` | Friendly female | Science explainers (default EN) |
| `en-US-AriaNeural` | Natural female | General content |
| `en-US-GuyNeural` | Natural male | General content |
| `en-US-EmmaMultilingualNeural` | Multilingual female | Cross-language content |
| `en-US-AndrewMultilingualNeural` | Multilingual male | Cross-language content |
| `en-US-AvaMultilingualNeural` | Multilingual female | — |
| `en-US-BrianMultilingualNeural` | Multilingual male | — |
| `en-GB-SoniaNeural` | British female | UK-style content |
| `en-GB-RyanNeural` | British male | UK-style content |
| `en-AU-NatashaNeural` | Australian female | AU-style content |
| `en-AU-WilliamNeural` | Australian male | AU-style content |

## edge-tts — Japanese Voices

| Voice ID | Gender | Notes |
|----------|--------|-------|
| `ja-JP-NanamiNeural` | Female | Natural, warm |
| `ja-JP-KeitaNeural` | Male | Natural |
| `ja-JP-AoiNeural` | Female | Lively |
| `ja-JP-DaichiNeural` | Male | Calm |
| `ja-JP-MayuNeural` | Female | Soft |
| `ja-JP-NaokiNeural` | Male | Energetic |
| `ja-JP-ShioriNeural` | Female | Friendly |

## edge-tts — Korean Voices

| Voice ID | Gender |
|----------|--------|
| `ko-KR-SunHiNeural` | Female |
| `ko-KR-InJoonNeural` | Male |
| `ko-KR-BongJinNeural` | Male |
| `ko-KR-GookMinNeural` | Male |
| `ko-KR-JiMinNeural` | Female |
| `ko-KR-SeoyeonNeural` | Female |
| `ko-KR-YuJinNeural` | Female |

## edge-tts — Other Languages

| Voice ID | Language | Gender |
|----------|----------|--------|
| `fr-FR-DeniseNeural` | French | Female |
| `fr-FR-HenriNeural` | French | Male |
| `de-DE-KatjaNeural` | German | Female |
| `de-DE-ConradNeural` | German | Male |
| `es-ES-ElviraNeural` | Spanish (Spain) | Female |
| `es-MX-DaliaNeural` | Spanish (Mexico) | Female |
| `pt-BR-FranciscaNeural` | Portuguese (Brazil) | Female |
| `pt-PT-RaquelNeural` | Portuguese (Portugal) | Female |
| `ar-SA-ZariyahNeural` | Arabic | Female |
| `hi-IN-SwaraNeural` | Hindi | Female |
| `ru-RU-SvetlanaNeural` | Russian | Female |
| `it-IT-ElsaNeural` | Italian | Female |
| `nl-NL-ColetteNeural` | Dutch | Female |
| `pl-PL-ZofiaNeural` | Polish | Female |
| `tr-TR-EmelNeural` | Turkish | Female |
| `vi-VN-HoaiMyNeural` | Vietnamese | Female |
| `th-TH-PremwadeeNeural` | Thai | Female |
| `id-ID-GadisNeural` | Indonesian | Female |

## edge-tts Rate & Pitch Guide

```python
# Rate: -50% (very slow) to +100% (very fast)
# Default for science videos: -5% (slightly slower for clarity)
# For fast-paced content: +10% to +20%
# For elderly/educational: -15% to -20%

# Pitch: -50Hz to +50Hz
# Default: +0Hz (natural)
# Higher pitch: +5Hz to +15Hz (more energetic)
# Lower pitch: -5Hz to -15Hz (more authoritative)

VOICE_CONFIGS = {
    "science_zh": {"voice": "zh-CN-XiaoxiaoNeural", "rate": "-5%", "pitch": "+0Hz"},
    "news_zh":    {"voice": "zh-CN-YunyangNeural",  "rate": "+0%", "pitch": "+0Hz"},
    "youth_zh":   {"voice": "zh-CN-XiaoyiNeural",   "rate": "+5%", "pitch": "+5Hz"},
    "science_en": {"voice": "en-US-JennyNeural",    "rate": "-5%", "pitch": "+0Hz"},
    "formal_en":  {"voice": "en-US-GuyNeural",      "rate": "+0%", "pitch": "-5Hz"},
}
```

## Voice Cloning Engines

### F5-TTS
- **Reference audio**: 5–30s WAV/M4A of target voice
- **Languages**: Chinese + English
- **RTF**: ~18x on CPU, ~0.15x on GPU
- **Install**: `pip install f5-tts`
- **Model**: F5TTS_v1_Base (1286MB)

### CosyVoice2
- **Reference audio**: Any length WAV
- **Languages**: ZH/EN/JP/KR/DE/FR/ES/IT/RU + 18 Chinese dialects
- **Streaming**: Yes (150ms latency)
- **Emotion control**: Yes (via instruct mode)
- **Install**: `pip install cosyvoice`

### GPT-SoVITS
- **Reference audio**: 5s minimum
- **Languages**: ZH/EN/JP/KR/Cantonese
- **Quality**: Highest among open-source cloning models
- **Install**: See [GPT-SoVITS repo](https://github.com/RVC-Boss/GPT-SoVITS)
