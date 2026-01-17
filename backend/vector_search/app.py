from fastapi import FastAPI

app = FastAPI()
VECTOR_DB = []

@app.post("/index")
def index(data: dict):
    VECTOR_DB.extend(data["embeddings"])
    return {"indexed": len(data["embeddings"])}

@app.post("/search")
def search():
    return sorted(
        VECTOR_DB,
        key=lambda x: x["vector"],
        reverse=True
    )
