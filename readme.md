# 🎧 Voice Emotion Translator

An AI-powered Streamlit application that records or uploads voice, detects emotion, transcribes it, translates it into multiple languages, and speaks the translated text aloud using **Google Text-to-Speech (gTTS)**.

---

## 🚀 Features

- 🎙️ Record or upload voice  
- 🧠 Detect emotion (happy, sad, neutral, angry, etc.)  
- 🗣️ Convert speech to text  
- 🌍 Translate text into multiple languages  
- 🔊 Speak translations with emotion tone  
- 💻 User-friendly Streamlit interface  

---

## 🛠️ Tech Stack

| Function | Library |
|-----------|----------|
| UI | Streamlit |
| Speech Recognition | SpeechRecognition / Whisper |
| Translation | googletrans |
| Emotion Detection | HuggingFace Transformers |
| Text-to-Speech | gTTS |
| Audio Handling | sounddevice, scipy, librosa |
| Language | Python 3.10+ |

---

## 📁 Folder Structure

voice-translation-prototype/
│
├── app.py
├── requirements.txt
└── utils/
├── emotion.py
├── stt.py
├── translate.py
└── tts.py

---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/EmdadulShishir/voice-translation-prototype.git
cd voice-translation-prototype
2️⃣ Create Virtual Environment
python -m venv .venv
3️⃣ Activate Virtual Environment
.venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt
▶️ Run the App
streamlit run app.py

💡 How to Use

Choose Record Voice or Upload Audio File.

Select the target language (e.g., Bengali, French, Chinese).

Record or upload your voice.

The app will:

Detect emotion 🎭

Transcribe speech ✍️

Translate text 🌐

Speak the translated output 🔊

🌍 Supported Languages

| Language | Code    |
| -------- | ------- |
| French   | `fr`    |
| German   | `de`    |
| Spanish  | `es`    |
| Italian  | `it`    |
| Chinese  | `zh-CN` |
| Bengali  | `bn`    |

⚠️ Notes

Requires internet connection for translation and TTS.

If the message shows “⚠️ Speech engine busy”, wait a few seconds and try again.

Works best on Windows 10/11 or macOS.

👨‍💻 Author

Emdadul Shishir
AI Developer & Innovator
Built with ❤️ using Python, Streamlit, and Google APIs.

📜 License

This project is licensed under the MIT License.
⭐ Support

If you like this project, please ⭐ star this repository on GitHub and share it!

---

✅ This version is **100% ready for GitHub** — it includes installation, run guide, and author credit exactly in standard markdown format.

Would you like me to also give you a short `requirements.txt` file (to include in your repo)?
