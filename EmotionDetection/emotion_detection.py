"""
Emotion detection module using Watson NLP library.
"""
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the provided text and extracts emotion scores.
    """
    # Handle empty or invalid inputs
    if not text_to_analyze:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Split the long URL across two lines to satisfy Pylint's 100-character limit
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Add a timeout to prevent hanging requests
    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    # Task 7: Handle status code 400 (Bad Request/Empty Input)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # Task 3: Formatting the output
    response_dict = response.json()
    emotions = response_dict['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Find the highest scoring emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    