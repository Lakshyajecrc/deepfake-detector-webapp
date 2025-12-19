from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
import tensorflow as tf
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Temporary folder for uploads
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Load your trained model (ensure 'deepfake_model.h5' is in the root folder)
model = tf.keras.models.load_model('deepfake_model.h5')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def detect_deepfake(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (128, 128)) / 255.0
    img = np.expand_dims(img, axis=0)
    prediction = model.predict(img)[0][0]
    return "Fake" if prediction > 0.5 else "Real", prediction

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '' or not allowed_file(file.filename):
            return redirect(request.url)
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        result, confidence = detect_deepfake(filepath)
        os.remove(filepath)  # Clean up uploaded file
        return render_template('result.html', result=result, confidence=f"{confidence:.2f}", filename=filename)
    return render_template('upload.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # For Heroku deployment
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(host='0.0.0.0', port=port, debug=False)  # Debug off for production