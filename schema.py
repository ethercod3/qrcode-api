from pydantic import BaseModel
from enum import Enum, auto


class ErrorCorrection(Enum):
    ERROR_CORRECT_M = 0
    ERROR_CORRECT_L = auto()
    ERROR_CORRECT_H = auto()
    ERROR_CORRECT_Q = auto()


class QRCodeRequest(BaseModel):
    data: str
    error_correction: ErrorCorrection = ErrorCorrection.ERROR_CORRECT_M
    version: int = 1
    box_size: int = 10
    border: int = 1
    back_color: str = "white"
    fill_color: str = "black"
