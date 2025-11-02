# utils/emotion.py
from transformers import pipeline

def load_emotion_model():
    """
    Load a public HuggingFace model for audio emotion recognition.
    Returns a pipeline that predicts emotions from audio files.
    """
    # Public model (works on CPU)
    classifier = pipeline(
        task="audio-classification",
        model="superb/wav2vec2-base-superb-er"
    )
    return classifier

def predict_emotion(classifier, audio_file):
    """
    Predict emotion from a given audio file using the classifier.
    """
    result = classifier(audio_file)[0]
    label = result["label"]
    confidence = round(result["score"], 2)
    return label, confidence
