from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

model = tf.keras.models.load_model('C:/Users/adrij/OneDrive/Desktop/skin-recommendation/TDL/skinAcneModel.h5')

def load_preprocess_image(image_data):
    image = Image.open(BytesIO(base64.b64decode(image_data)))
    image = image.resize((224, 224))
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)
    return image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['image']
    image_data = data.split(',')[1]
    image = load_preprocess_image(image_data)
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    return jsonify({'predicted_class': int(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True)
