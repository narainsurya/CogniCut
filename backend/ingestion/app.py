from fastapi import FastAPI

app = FastAPI()

@app.post("/transcribe")
def transcribe(data: dict):
    # Hackathon-safe: mock transcript
    return {
        "segments": [
            {"start": 0, "end": 20, "text": "This is an important concept"},
            {"start": 25, "end": 45, "text": "This explains the core idea"},
            {"start": 50, "end": 70, "text": "This is the conclusion"}
        ]
    }
