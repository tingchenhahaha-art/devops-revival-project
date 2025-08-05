from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello DevOps Revival!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
