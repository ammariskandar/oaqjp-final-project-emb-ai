"""
server.py

This module sets up a Flask web server that provides endpoints for emotion detection.
It integrates with the EmotionDetection package to analyze text and return emotional insights.

By Ammar Iskandar
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Handles requests to the /emotionDetector endpoint.

    Retrieves the text to analyze from the request, passes it to the emotion_detector function,
    and returns the detected emotions and the dominant emotion as a formatted string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    anger = response.get('anger', 'N/A')
    disgust = response.get('disgust', 'N/A')
    fear = response.get('fear', 'N/A')
    joy = response.get('joy', 'N/A')
    sadness = response.get('sadness', 'N/A')
    dominant_emotion = response.get('dominant_emotion', 'N/A')
    if dominant_emotion is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is "
        f"{dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Handles requests to the root endpoint.

    Renders the index.html template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
