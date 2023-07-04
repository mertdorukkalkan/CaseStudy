import json

from fastapi.exceptions import HTTPException
from fastapi import UploadFile, APIRouter

from business.translate_service import translate_data

from models.model import Data

router = APIRouter()


@router.post("/translated")
async def gpt(data: Data):
    data_json = json.loads(data.json())
    translated_data = translate_data(data_json)
    return translated_data

@router.post("/translatedFromJSON")
async def gpt(file: UploadFile):
    if file.content_type != "application/json":
        raise HTTPException(400, detail="Invalid Document Type")
    data = json.loads(file.file.read())
    translated_data = translate_data(data)
    return translated_data
