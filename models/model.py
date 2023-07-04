from pydantic import BaseModel
from typing import Optional


class NestedData(BaseModel):
    Name: str
    Email: str
    Gender: str

class Data(BaseModel):
    Name: str
    Email: str
    Gender: str
    Company: str
    Title: Optional[str]
    Unit: str
    Age: int
    Danger: str
    NestedData: Optional[NestedData]
