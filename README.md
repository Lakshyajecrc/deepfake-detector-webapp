# Deepfake Detector Web App

A simple web-based deepfake image detector built with Flask, TensorFlow, and OpenCV. Upload an image to check if it's real or fake.

## Features
- Upload images (PNG, JPG, JPEG).
- Real-time detection using a trained CNN model.
- Clean, responsive UI with Bootstrap.

## Live Demo
Try it out: [Live Demo Link](https://your-app.herokuapp.com) (replace with your Heroku URL)

## Setup (Local)
1. Clone the repo: `git clone https://github.com/yourusername/deepfake-detector-webapp.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Train and place your model: Run the training script from the code (save as `deepfake_model.h5` in root).
4. Run the app: `python app.py`
5. Open `http://127.0.0.1:5000/` in your browser.

## Usage
- Upload an image on the homepage.
- View the result (Real/Fake) with confidence score.

## Deployment
- Deployed on Heroku for easy access.
- See Procfile for deployment config.

## Limitations
- Model accuracy depends on training data.
- For videos, extend with frame extraction.
- Ethical use only: Do not misuse for harmful purposes.

## Tech Stack
- Backend: Python, Flask, TensorFlow, OpenCV
- Frontend: HTML, CSS, Bootstrap

## License
MIT License. See LICENSE for details.

## Contributing
Pull requests welcome! Report issues on GitHub.
