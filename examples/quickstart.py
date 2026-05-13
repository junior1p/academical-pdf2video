#!/usr/bin/env python3
"""
academical-pdf2video — Quick Start Example
Converts a PDF paper to a ~2min Chinese science video using edge-tts + Remotion.

Usage:
    python examples/quickstart.py --pdf paper.pdf --voice zh-CN-XiaoxiaoNeural
"""

import argparse
import asyncio
import json
import math
import os
import subprocess

import nest_asyncio
nest_asyncio.apply()

import edge_tts

# ─── Configuration ────────────────────────────────────────────────────────────

DEFAULT_VOICE = "zh-CN-XiaoxiaoNeural"
DEFAULT_RATE = "-5%"
FPS = 30
BUFFER_S = 2.5  # seconds of buffer after each TTS segment
BGM_VOLUME = 0.18

# ─── Step 1: Write your scene scripts ─────────────────────────────────────────
# Replace these with content extracted from your PDF

SCRIPTS = {
    "sc0": "",  # Cover: hook question (leave empty for title card)
    "sc1": "这篇论文来自斯坦福大学，研究了大语言模型在蛋白质设计中的应用。",
    "sc2": "研究团队构建了一个包含76个任务的基准测试，覆盖从头设计到功能预测的全流程。",
    "sc3": "测试结果显示，GPT-5在工具调用模式下达到了56分，而专家基线为61分。",
    "sc4": "最令人惊讶的发现是：模型的失败不是能力问题，而是行为问题。",
    "sc5": "通过简单的提示词干预，GPT-5的得分提升了15.9分，提升幅度高达28%。",
    "sc6": "这说明当前的LLM已经具备了足够的知识，缺少的是正确的行为引导。",
    "sc7": "这不是能力瓶颈，而是行为瓶颈。AI蛋白质设计的下一步，在于对齐。",
}

# ─── Step 2: Generate TTS ─────────────────────────────────────────────────────

async def generate_tts(scripts: dict, out_dir: str, voice: str, rate: str):
    os.makedirs(out_dir, exist_ok=True)
    for key, text in scripts.items():
        if not text:
            continue
        out_path = os.path.join(out_dir, f"{key}.mp3")
        comm = edge_tts.Communicate(text, voice, rate=rate)
        await comm.save(out_path)
        print(f"  Generated: {out_path}")

# ─── Step 3: Measure durations ────────────────────────────────────────────────

def get_duration(path: str) -> float:
    if not os.path.exists(path):
        return 5.0  # default for empty scenes
    r = subprocess.run(
        f'ffprobe -v quiet -print_format json -show_streams "{path}"',
        shell=True, capture_output=True, text=True
    )
    streams = json.loads(r.stdout).get("streams", [])
    return float(streams[0]["duration"]) if streams else 5.0

# ─── Step 4: Compute scene frames ─────────────────────────────────────────────

def compute_frames(durations: dict) -> dict:
    frames = {}
    for key, dur in durations.items():
        frames[key] = math.ceil((dur + BUFFER_S) * FPS / 10) * 10
    return frames

# ─── Step 5: Mix BGM ──────────────────────────────────────────────────────────

def mix_bgm(tts_dir: str, bgm_path: str, out_path: str, video_dur: float):
    # Concatenate TTS
    concat_file = os.path.join(tts_dir, "concat.txt")
    with open(concat_file, "w") as f:
        for key in SCRIPTS.keys():
            mp3 = os.path.join(tts_dir, f"{key}.mp3")
            if os.path.exists(mp3):
                f.write(f"file '{mp3}'\n")

    tts_full = os.path.join(tts_dir, "tts_full.mp3")
    subprocess.run(
        f'ffmpeg -y -f concat -safe 0 -i "{concat_file}" -c:a libmp3lame -q:a 2 "{tts_full}"',
        shell=True, check=True
    )

    # Mix with BGM
    subprocess.run(
        f'ffmpeg -y -i "{tts_full}" -i "{bgm_path}" \'
        f'-filter_complex "[1:a]volume={BGM_VOLUME},afade=t=in:st=0:d=3,\'
        f'afade=t=out:st={video_dur-5}:d=5,atrim=0:{video_dur},apad=whole_dur={video_dur}[bgm];\'
        f'[0:a]apad=whole_dur={video_dur}[tts];\'
        f'[tts][bgm]amix=inputs=2:duration=longest:dropout_transition=3[out]" \'
        f'-map "[out]" -t {video_dur} -c:a libmp3lame -q:a 2 "{out_path}"',
        shell=True, check=True
    )
    print(f"  Mixed audio: {out_path}")

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="PDF to Video Quick Start")
    parser.add_argument("--pdf", required=True, help="Path to PDF file")
    parser.add_argument("--voice", default=DEFAULT_VOICE, help="edge-tts voice ID")
    parser.add_argument("--rate", default=DEFAULT_RATE, help="TTS rate (e.g. -5%)")
    parser.add_argument("--bgm", default=None, help="Path to BGM MP3 (optional)")
    parser.add_argument("--out", default="output.mp4", help="Output video path")
    args = parser.parse_args()

    work_dir = "/workspace/pdf2video_quickstart"
    audio_dir = os.path.join(work_dir, "audio")
    os.makedirs(work_dir, exist_ok=True)

    print("\n[1/4] Generating TTS audio...")
    asyncio.get_event_loop().run_until_complete(
        generate_tts(SCRIPTS, audio_dir, args.voice, args.rate)
    )

    print("\n[2/4] Computing scene durations...")
    durations = {key: get_duration(os.path.join(audio_dir, f"{key}.mp3"))
                 for key in SCRIPTS.keys()}
    frames = compute_frames(durations)
    total_frames = sum(frames.values())
    video_dur = total_frames / FPS
    print(f"  Total duration: {video_dur:.1f}s ({total_frames} frames)")

    print("\n[3/4] Mixing audio...")
    if args.bgm and os.path.exists(args.bgm):
        bgm_path = args.bgm
    else:
        print("  No BGM provided — skipping BGM mix")
        bgm_path = None

    audio_final = os.path.join(audio_dir, "audio_final.mp3")
    if bgm_path:
        mix_bgm(audio_dir, bgm_path, audio_final, video_dur)
    else:
        # Just concatenate TTS
        concat_file = os.path.join(audio_dir, "concat.txt")
        with open(concat_file, "w") as f:
            for key in SCRIPTS.keys():
                mp3 = os.path.join(audio_dir, f"{key}.mp3")
                if os.path.exists(mp3):
                    f.write(f"file '{mp3}'\n")
        subprocess.run(
            f'ffmpeg -y -f concat -safe 0 -i "{concat_file}" -c:a libmp3lame -q:a 2 "{audio_final}"',
            shell=True, check=True
        )

    print("\n[4/4] Done! Next steps:")
    print(f"  - Audio: {audio_final}")
    print(f"  - Frames config: {json.dumps(frames, indent=2)}")
    print(f"  - Build Remotion or HyperFrames composition with these frame counts")
    print(f"  - See SKILL.md for complete rendering instructions")

if __name__ == "__main__":
    main()
