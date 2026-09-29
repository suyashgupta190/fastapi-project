from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "fastapi is running successfully!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/hello/{name}")
async def hello(name: str):
    return {"message": f"Hello, {name}!"}
