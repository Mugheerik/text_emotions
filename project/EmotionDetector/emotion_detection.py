import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 200:
        emotion_predictions = json.loads(response.text)["emotionPredictions"][0]
        emotion_scores = emotion_predictions["emotion"]
        dominant_emotion = max(emotion_scores.keys(), key=(lambda k: emotion_scores[k]))


        emotion_scores_dict = {
            "anger": emotion_scores["anger"],
            "disgust": emotion_scores["disgust"],
            "fear": emotion_scores["fear"],
            "joy": emotion_scores["joy"],
            "sadness": emotion_scores["sadness"],
            "dominant_emotion": dominant_emotion
        }

    elif response.status_code == 400:
        emotion_scores_dict = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    
    return(emotion_scores_dict)

    