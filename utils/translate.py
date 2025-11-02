from googletrans import Translator

translator = Translator()

def translate(text, target_lang="fr"):
    lang_map = {
        "French": "fr",
        "German": "de",
        "Spanish": "es",
        "Italian": "it",
        "Chinese": "zh-cn",
        "Bengali": "bn"
    }
    code = lang_map.get(target_lang, "fr")
    translated = translator.translate(text, dest=code)
    return translated.text

