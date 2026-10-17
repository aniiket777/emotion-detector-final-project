"""Flask server for the Emotion Detector application."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Renders the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Handles emotion detection requests for input text.

    Returns:
        tuple[str, int]: Formatted analysis result or error message with HTTP status.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    is_blank = text_to_analyze is None or not text_to_analyze.strip()
    text_length = len(text_to_analyze) if text_to_analyze is not None else 0

    print(
        f"[DIAGNOSTIC] /emotionDetector query received: "
        f"length={text_length}, is_blank={is_blank}"
    )

    if is_blank:
        return "Invalid text! Please try again!", 400

    response = emotion_detector(text_to_analyze)

    if response.get("dominant_emotion") is None:
        return "Emotion detection service is currently unavailable. Please try again later.", 502

    formatted_output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return formatted_output, 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
