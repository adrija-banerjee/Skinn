from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

model = tf.keras.models.load_model('C:/Users/adrij/OneDrive/Desktop/skin-recommendation/TDL/skinAcneModel.h5')
model2 = tf.keras.models.load_model('C:/Users/adrij/OneDrive/Desktop/skin-recommendation/TDL/model.h5')

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
     # Predict using model 1 (acne level)
    predictions_acne = model.predict(image)
    predicted_class_acne = np.argmax(predictions_acne, axis=1)[0]

    # Predict using model 2 (skin type: dry, oily, normal)
    predictions_skin_type = model2.predict(image)
    predicted_class_skin_type = np.argmax(predictions_skin_type, axis=1)[0]

     # Map the predicted_class_skin_type to a human-readable label
    skin_type_labels = ["Dry", "Oily", "Normal"]
    skin_type_label = skin_type_labels[predicted_class_skin_type]

    return jsonify({
        'predicted_class_acne': int(predicted_class_acne),
        'predicted_class_skin_type': skin_type_label
    })

if __name__ == '__main__':
    app.run(debug=True)
