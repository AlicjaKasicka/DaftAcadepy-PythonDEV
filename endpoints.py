from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"start": "1970-01-01"}

@app.get("/method")
def method():
    return 0