import qrcode
import random
import string


def generateRandomQr():
    # Generate random string
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=10))

    img = qrcode.make(random_string)
    type(img)  # qrcode.image.pil.PilImage
    # img.save(f"../resources/{random_string}.png")
    print(random_string)
    return img, random_string
