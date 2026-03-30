from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse({
        "hasMessage": True,
        "title": "v1.3 successfully launched.",
        "message": "I have successfully launched a new version v1.3. V1.3 presents AI summery as the major feature of the update. The version also brings enhancements in user experience and plugin stability. Thanks for your continued support and love for AI voice dictation jieshuo plugin.",
        "hasLink": True,
        "link": "https://t.me/blindtechvisionary"
    })