import os
from io import BytesIO
from random import choice
from string import ascii_lowercase as letters

import numpy as np
import requests
import tensorflow as tf
from PIL import Image
from flask import Flask, request, render_template

from utils import load_model

THRESHOLD = 123

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = 'static'

app.secret_key = 'secret'
app.debug = False

model = load_model('model/architecture.json', 'model/weights.h5')

os.makedirs(app.config["IMAGE_UPLOADS"], exist_ok=True)


@app.route('/')
def index():
    url = request.args.get('url')
    if not url:
        return render_template('main.html')

    resp = requests.get(url)
    original_image = ''.join(choice(letters) for _ in range(10)) + '.png'

    img = Image.open(BytesIO(resp.content)).resize((320, 320))
    img.save(os.path.join(app.config['IMAGE_UPLOADS'], original_image))

    tensor_data = tf.convert_to_tensor(np.array(img)[..., 0:3])
    predicted = model.predict(np.expand_dims(tensor_data, axis=0)).round()

    predicted[predicted == 1] = THRESHOLD

    result_image = f'segmented-{original_image}'
    Image.fromarray(predicted.squeeze()).convert('L').save(
        os.path.join(app.config['IMAGE_UPLOADS'], result_image)
    )

    return render_template(
        'main.html',
        url=url, 
        original_image=original_image,
        result_image=result_image,
    )


if __name__ == '__main__':
    app.run(use_reloader=True)
