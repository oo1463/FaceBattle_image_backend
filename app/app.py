from flask import Flask, render_template, jsonify, request, Response
from flask_restful import Resource, Api
import numpy as np
# import tensorflow
import cv2
import json
app = Flask(__name__)


@app.route("/images", methods=['POST'])
def predict():
    req = request
    # uploaded_files = request.files.getlist("file")
    # print(req.header)

    nparr = np.fromstring(req.data, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(img)

    response = {'message': 'image received. size={}x{}x{}'.format(img.shape[1], img.shape[0], img.shape[2])}

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
