from fastapi import FastAPI

class HerokuApp:
    app_url = "https://app-basics.herokuapp.com/"  # Fill your heroku app url here


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}