from fastapi import FastAPI
from schema import QRCodeRequest
from qrcode import QRCode
import io
import base64

app = FastAPI()


@app.post("/qr")
async def generate_qr(request: QRCodeRequest):
    model_dump: dict = request.model_dump()

    qr_data: str = model_dump.pop("data")
    back_color: str = model_dump.pop("back_color")
    fill_color: str = model_dump.pop("fill_color")

    qr_code: QRCode = QRCode(**model_dump)
    qr_code.add_data(qr_data)

    image = qr_code.make_image(back_color=back_color, fill_color=fill_color)
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str: bytes = base64.b64encode(buffered.getvalue()).decode()
    return img_str
