from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print("Abhishek")
    return {"message": "Hello Test"}