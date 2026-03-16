import cv2
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("D:\PROJECTS\AI-Mood-Mate\Emotion-Detection-and-Music-Recommendation-System\models\emotion_cnn_model.keras")

emotion_labels = [
    "angry",
    "disgust",
    "fear",
    "happy",
    "sad",
    "surprise",
    "neutral"
]

def predict_emotion(image):

    img = cv2.resize(image, (48,48))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img / 255.0

    img = img.reshape(1,48,48,1)

    prediction = model.predict(img)

    emotion = emotion_labels[np.argmax(prediction)]

    return emotion