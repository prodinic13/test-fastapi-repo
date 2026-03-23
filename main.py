from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from test-fastapi-repo!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}


@app.get("/ping")
def ping():
    return {"pong": True}


@app.get("/version")
def version():
    return {"version": "1.0.0"}


@app.get("/echo/{message}")
def echo(message: str):
    return {"echo": message}
