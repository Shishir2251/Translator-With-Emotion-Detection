import streamlit as st
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import tempfile
from utils import emotion, stt, translate, tts

st.set_page_config(page_title="🎧 Voice Emotion Translator", layout="centered")
st.title("🎙️ AI Voice Translator with Emotion")

# ---------------------------
# Load models
# ---------------------------
@st.cache_resource
def load_models():
    emo_model = emotion.load_emotion_model()
    return emo_model

classifier = load_models()

# Language selection
target_lang = st.selectbox(
    "Translate to:",
    ["French", "German", "Spanish", "Italian", "Chinese", "Bengali"]
)


# ---------------------------
# Recording duration
# ---------------------------
duration = st.slider("Recording duration (seconds)", 3, 10, 5)

# ---------------------------
# Input Method: Record or Upload
# ---------------------------
input_method = st.radio("Choose input method:", ("🎤 Record Voice", "📁 Upload Audio File"))

audio_path = None  # Initialize variable

if input_method == "🎤 Record Voice":
    if st.button("Start Recording"):
        st.info("🎙️ Recording... Speak now!")
        fs = 16000
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        st.success("✅ Recording complete!")
        recording = np.int16(recording * 32767)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            write(tmp.name, fs, recording)
            audio_path = tmp.name

        st.audio(audio_path, format="audio/wav")

elif input_method == "📁 Upload Audio File":
    uploaded_file = st.file_uploader("📂 Upload an audio file (WAV or MP3)", type=["wav", "mp3"])
    if uploaded_file is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            tmp.flush()
            audio_path = tmp.name

        st.success("✅ File uploaded successfully!")
        st.audio(audio_path, format="audio/wav")

# ---------------------------
# Process audio if available
# ---------------------------
if audio_path is not None:

    # Emotion detection
    with st.spinner("Detecting emotion..."):
        label, confidence = emotion.predict_emotion(classifier, audio_path)
    st.success(f"Emotion: **{label.upper()}** ({confidence*100:.1f}%)")

    # Speech-to-text
    with st.spinner("Transcribing..."):
        text = stt.transcribe(audio_path)
    st.text_area("Transcription", value=text, height=100)

   # ---------------------------
# Translation
# ---------------------------
    with st.spinner("Translating..."):
        translated_text = translate.translate(text, target_lang=target_lang)
        st.text_area("Translation", value=translated_text, height=100)

    # ---------------------------
    # Text-to-speech
    # ---------------------------
    with st.spinner("Speaking..."):
        try:
            tts.speak(translated_text, emotion=label)

            st.success("✅ Voice generated with emotion!")
        except RuntimeError:
            st.warning("⚠️ TTS engine was busy. Please try again.")
