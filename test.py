from fastapi import FastAPI
import pandas

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
