import flask
from flask import request, jsonify
import numpy as np
import cv2
import base64
import io
import standalone
from PIL import Image

from __init__ import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/inference/road_occupied', methods=['POST'])
def inference():
    if request.method == 'POST':
        data = request.get_json()
        image = data['image']
        image = base64.b64decode(image)
        inference = standalone.Predict()
        r_image, r_boxes, r_classes, r_scores = inference.predict(image)
        r_image = cv2.cvtColor(np.asarray(r_image), cv2.COLOR_RGB2BGR)
        _, r_image = cv2.imencode('.jpg', r_image)
        r_image = base64.b64encode(r_image)
        r_image = r_image.decode('utf-8')
        # return jsonify({'image': r_image, 'boxes': r_boxes.tolist(), 'classes': r_classes.tolist(), 'scores': r_scores.tolist()})
        return jsonify({
            'code': 200,
            'message': 'success',
            'data': {
                'image': r_image,
                'boxes': r_boxes.tolist(),
                'classes': r_classes.tolist(),
                'scores': r_scores.tolist()
                }
            })
    else:
        logger.error("Request method is not POST")
        return jsonify({
            'code': 400,
            'message': 'Request method is not POST',
            'data': {}
            })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)