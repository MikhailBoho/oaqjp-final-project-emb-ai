"""
Flask server for the Emotion Detection application.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render the main index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the provided text and return the emotion scores.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the Watson API
    response = emotion_detector(text_to_analyze)

    # Task 7: Error handling for invalid text
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    # Format the final output string
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    