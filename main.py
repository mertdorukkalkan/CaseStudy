

from fastapi import FastAPI, UploadFile
from web_api import translate_controller, upload_json_controller

app = FastAPI()

app.include_router(translate_controller.router)
app.include_router(upload_json_controller.router)



@app.get("/")
async def say_hello():
    return 'hello'
