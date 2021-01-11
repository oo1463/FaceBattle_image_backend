from flask import Flask, jsonify, request
import numpy as np
from tensorflow.keras.models import load_model
import cv2
import json
from PIL import Image


app = Flask(__name__)

model = load_model('./Face_model')


@app.route("/images", methods=['POST'])
def get_images():
    file1 = request.files['image1'].read()
    file2 = request.files['image2'].read()

    img1 = Image.open(request.files['image1'])
    img1 = np.array(img1)
    img1 = cv2.resize(img1, (96, 96))

    img2 = Image.open(request.files['image2'])
    img2 = np.array(img2)
    img2 = cv2.resize(img2, (96, 96))

    print(img1.shape)
    print(img2.shape)

    img1 = img1.reshape(1, 96, 96, 3)
    pred_1 = model.predict(img1)

    img2 = img1.reshape(1, 96, 96, 3)
    pred_2 = model.predict(img2)

    mx1 = np.argmax(pred_1)
    mx2 = np.argmax(pred_2)

    print(mx1, pred_1.max())
    print(mx2, pred_2.max())

    response = {'image1_score': '{}'.format(mx1), 'image2_score': '{}'.format(mx2)}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
