from flask import Flask, request, g, jsonify
import sqlite3
import qr_generator
from io import BytesIO
import base64

app = Flask(__name__)
last_code = ""


@app.route("/")
def index():
    return "welcomming route"


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, format="PNG")  # You can choose other formats like JPEG
    img_io.seek(0)
    encoded_data = base64.b64encode(img_io.getvalue()).decode("utf-8")
    return f'<img src="data:image/png;base64,{encoded_data}" />'


@app.route("/verify", methods=["POST"])
def verify():
    if request.method == "POST":
        data = request.get_json()
        key = data.get("key")
        global last_code
        return "gecerli" if key == last_code else "gecersiz"


@app.route("/qr", methods=["GET"])
def qr():
    if request.method == "GET":
        global last_code
        img, last_code = qr_generator.generateRandomQr()
        return serve_pil_image(img)


# run the application on port 5000 and static ip address.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
