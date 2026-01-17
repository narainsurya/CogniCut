from fastapi import FastAPI

app = FastAPI()

@app.post("/plan")
def plan(data: dict):
    segments = data["segments"]
    scored = []

    for s in segments:
        score = (s["end"] - s["start"]) + len(s["text"])
        scored.append({**s, "score": score})

    scored.sort(key=lambda x: x["score"], reverse=True)
    return {"highlights": scored[:3]}
