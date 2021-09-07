import os
import json

from flask import Flask, request
from flask_cors import CORS, cross_origin

from images_service import ImageService

app = Flask(__name__)
CORS(app)

ImageService = ImageService()

@app.route("/ping")
def ping():
    return "Pong!"

@app.route("/images", methods=["GET"])
def images():
    response, code = ImageService.get_all(request)

    return json.dumps(response), code, {"Content-Type" : "application/json"}

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True, port=int(os.environ.get("PORT", 5000)))