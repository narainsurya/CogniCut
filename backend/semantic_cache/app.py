from fastapi import FastAPI

app = FastAPI()
CACHE = {}

@app.post("/check")
def check(data: dict):
    key = data["key"]
    if key in CACHE:
        return {"hit": True, "value": CACHE[key]}
    return {"hit": False}

@app.post("/store")
def store(data: dict):
    CACHE[data["key"]] = data["value"]
    return {"stored": True}
