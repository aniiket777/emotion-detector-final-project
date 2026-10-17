"""Emotion detection module using IBM Watson NLP EmotionPredict service."""
import requests


def emotion_detector(text_to_analyze):
    """Analyzes emotions from input text using the IBM Watson NLP service.

    Args:
        text_to_analyze (str): Text string to be evaluated for emotions.

    Returns:
        dict: Emotion scores for anger, disgust, fear, joy, sadness,
              and dominant_emotion. Returns None for all values if
              input is blank, invalid, or an error occurs.
    """
    result = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    if not text_to_analyze or not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return result

    url = (
        'https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}
    payload = {'raw_document': {'text': text_to_analyze}}

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            emotions = data['emotionPredictions'][0]['emotion']
            emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
            result = {key: emotions.get(key) for key in emotion_keys}
            result['dominant_emotion'] = max(
                emotion_keys,
                key=lambda k: result[k] if result[k] is not None else float('-inf')
            )
    except (requests.exceptions.RequestException, ValueError, KeyError, IndexError):
        pass

    return result
