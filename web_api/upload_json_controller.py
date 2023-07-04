from fastapi.exceptions import HTTPException
from fastapi import UploadFile, APIRouter
import json

from business.convert_json_service import ConvertJson

router = APIRouter()
convert_json = ConvertJson()

@router.post("/uploadJSON")
async def upload_file(file: UploadFile):
    if file.content_type != "application/json":
        raise HTTPException(400,detail="Invalid Document Type")
    data = json.loads(file.file.read())
    new_data = await convert_json.upload_json(data)
    return new_data[0]['children']
