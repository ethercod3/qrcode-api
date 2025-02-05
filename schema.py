from pydantic import BaseModel


class QRCodeRequest(BaseModel):
    data: str
    error_correction: int = 0
    version: int = 1
    box_size: int = 10
    border: int = 1
    back_color: str = "white"
    fill_color: str = "black"
