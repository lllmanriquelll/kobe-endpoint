from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def read_root(response: Response):
    response.headers["kobe-endpoint"] = "omnivector"
    return {"message": "Hello World"}
