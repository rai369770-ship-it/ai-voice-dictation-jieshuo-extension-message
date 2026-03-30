from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({
        "hasMessage": True,
        "title": "v1.3 launch",
        "message": "Version 1.3 is pack of brand new features on the extension. I am very excited to share the new version. Visit our telegram channel for future updates and features.",
        "hasLink": True,
        "link": "t.me/blindtechvisionary"
    })