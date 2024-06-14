from flask import Flask, request, g, jsonify
import sqlite3
import qr_generator
from io import BytesIO
import base64
from actionsmodel import Actions
from db_qrcode_service import DbQrcodeService
from db_actions_service import DbActionsService
from qrcodemodel import QrCode


# run the application on port 5000 and static ip address.
class Service:
    def __init__(self):
        self.app = Flask(__name__)
        self.last_code = None
        self.setup_routes()
        self.dbService = DbQrcodeService()
        self.dbActionsService = DbActionsService()

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
                self.dbService.add(
                    action=Actions(id=1), code=self.last_code.code
                )  # db addition
                return self.serve_pil_image(img)

        @self.app.route("/get_all_codes", methods=["GET"])
        def get_all():
            if request.method == "GET":
                codes = self.dbService.get_all()
                serialized_codes = [code.serialize() for code in codes]
                return jsonify(serialized_codes)

        @self.app.route("/get_all_actions", methods=["GET"])
        def get_all_actions():
            if request.method == "GET":
                actions = self.dbActionsService.get_all()
                serialized_actions = [action.serialize() for action in actions]
                return jsonify(serialized_actions)

    def run(self):
        self.app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    service = Service()
    service.run()
