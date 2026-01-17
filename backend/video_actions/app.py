from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/clip")
def clip(data: dict):
    clips = []
    for i, h in enumerate(data["highlights"]):
        out = f"clip_{i}.mp4"
        subprocess.call([
            "ffmpeg", "-y",
            "-ss", str(h["start"]),
            "-to", str(h["end"]),
            "-i", data["video_path"],
            out
        ])
        clips.append(out)
    return {"clips": clips}
