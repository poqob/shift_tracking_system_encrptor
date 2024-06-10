import qrcode
import io
import random
import string


def generateRandomQr():
    # Generate random string
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))

    img = qrcode.make(random_string)
    type(img)  # qrcode.image.pil.PilImage
    img.save("some_file.png")
    return img, random_string
