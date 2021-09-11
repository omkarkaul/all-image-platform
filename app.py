import os
import json
import logging

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
    app.logger.debug(f"REQUEST ARGS: {dict(request.args)}")
    response, code = ImageService.get_all(request)
    app.logger.debug(f"RESPONSE CODE: {code}\n")

    return json.dumps(response), code, {"Content-Type" : "application/json"}

if __name__ == "__main__":
    print("Run \"start.sh\" to start the All Image service, do not run this file directly")
else:
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)