from flask import Flask, request, g, jsonify
import sqlite3
import qr_generator
from io import BytesIO
import base64
from db_service import DbService


# run the application on port 5000 and static ip address.
class Service:
    def __init__(self):
        self.app = Flask(__name__)
        self.last_code = None
        self.setup_routes()
        self.dbService = DbService()

    def serve_pil_image(self, pil_img):
        img_io = BytesIO()
        pil_img.save(img_io, format="PNG")  # You can choose other formats like JPEG
        img_io.seek(0)
        encoded_data = base64.b64encode(img_io.getvalue()).decode("utf-8")
        return f'<img src="data:image/png;base64,{encoded_data}" />'

    def setup_routes(self):
        @self.app.route("/")
        def index():
            return "welcomming route"

        @self.app.route("/verify", methods=["POST"])
        def verify():
            if request.method == "POST":
                data = request.get_json()
                key = data.get("key")
                if self.dbService.get_by_code(key) is not None:
                    return key
                else:
                    return key + " is not found"

        @self.app.route("/qr", methods=["GET"])
        def qr():
            if request.method == "GET":
                img, self.last_code = qr_generator.generateRandomQr()
                self.dbService.add(1, self.last_code)  # db addition
                return self.serve_pil_image(img)

        @self.app.route("/get_all", methods=["GET"])
        def get_all():
            if request.method == "GET":
                return jsonify(self.dbService.get_all())

    def run(self):
        self.app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    service = Service()
    service.run()
