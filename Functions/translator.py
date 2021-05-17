from google_trans_new import google_translator
from SPT.spt import Assistant, Voice


class Translator(Assistant, Voice):
    def __init__(self):
        super().__init__()
        self.translator_en = google_translator()

    def Spanish(self, voices=Voice(), x=Assistant()):
        print(voices.speak_en('what do you want to translate'))
        assistant = x.recognize_voice()
        t = self.translator_en.translate(assistant, lang_tgt='es')
        voices.speak_es(t)
        return t
