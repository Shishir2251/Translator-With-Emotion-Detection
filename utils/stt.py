from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa

# Local Whisper STT
processor = WhisperProcessor.from_pretrained("openai/whisper-small")
model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-small")

def transcribe(audio_file):
    audio, sr = librosa.load(audio_file, sr=16000)
    input_features = processor(audio, sampling_rate=sr, return_tensors="pt").input_features
    predicted_ids = model.generate(input_features)
    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    return transcription
