import unittest
from Functions.translator import Translator
from google_trans_new import google_translator

from SPT.spt import Voice, Assistant


class test_Translator(unittest.TestCase, Translator):

    def test_Spanish(self, voices=Voice(), x=Assistant()):
        # testing if the method works
        self.translator_en = google_translator()
        print(voices.speak_en('what do you want to translate'))
        # here receives the voice command in English
        assistant = x.recognize_voice()
        # here we check if it is not the same
        t = self.translator_en.translate(assistant, lang_tgt='es')
        voices.speak_es(t)
        return t

    def test_Spanish_NotEqual(self, voices=Voice(), x=Assistant()):
        # testing if what the Assistant receives is not the same what it returns.
        # example :
        # the assistant receives the voice command in English and when translating it,
        # it returns the result in the language previously assigned.
        self.translator_en = google_translator()
        print(voices.speak_en('what do you want to translate'))
        # here receives the voice command in English
        assistant = x.recognize_voice()
        # here it is translated
        t = self.translator_en.translate(assistant, lang_tgt='es')
        # here we check if it is not the same
        if self.assertNotEqual(assistant, t):
            voices.speak_es(t)
            return t
        else:
            print('equal')


if __name__ == '__main__':
    unittest.main()
