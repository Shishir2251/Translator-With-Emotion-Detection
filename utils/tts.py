import pyttsx3
import streamlit as st
import threading

def _speak_thread(text, emotion="neutral"):
    try:
        engine = pyttsx3.init()
        # Set voice rate or volume based on emotion (optional)
        if emotion == "happy":
            engine.setProperty("rate", 180)
        elif emotion == "sad":
            engine.setProperty("rate", 120)
        elif emotion == "angry":
            engine.setProperty("rate", 150)
        else:
            engine.setProperty("rate", 150)

        engine.say(text)
        engine.runAndWait()
        engine.stop()
        st.success("✅ Speech playback completed!")
    except Exception as e:
        st.warning(f"⚠️ TTS failed: {e}")

def speak(text, emotion="neutral"):
    # Run TTS in a separate thread so Streamlit is not blocked
    t = threading.Thread(target=_speak_thread, args=(text, emotion))
    t.start()

