import qrcode
import random
import string
from qrcodemodel import QrCode as QR


def generateRandomQr():
    # Generate random string
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))

    img = qrcode.make(random_string)
    type(img)  # qrcode.image.pil.PilImage
    # img.save(f"../resources/{random_string}.png")

    return (img, QR(code=random_string))  # return the image and the code
