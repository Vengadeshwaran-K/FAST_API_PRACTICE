from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to Vengi's Tech World!!!"