# Module docstring
"""
Flask server for emotion detection.
"""

from flask import Flask,render_template ,request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
# Function docstring for sent_analyzer()
def sent_analyzer():

    """Predict the emotion in a given text.

    Args:
    text_to_analyze: The text to analyze.

    Returns:
    A string containing the emotion detection results.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid Text! please try again"


    formatted_emotion_response = (
    f"For the given statement, the system response is 'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}."
)

    return formatted_emotion_response


@app.route("/")
# Function docstring for render_index_page()
def render_index_page():
    """Render the index page."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
# Add newline
