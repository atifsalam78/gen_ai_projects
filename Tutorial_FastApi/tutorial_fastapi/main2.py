from fastapi import FastAPI

app : FastAPI = FastAPI()

# @app.get("/hi/{who}")
# def greet(who):
#     return f"Hello, {who}"

@app.get("/hi")
def greet(who):
    return f"Hello, {who}"