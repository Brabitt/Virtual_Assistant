import speech_recognition as sr
import pyttsx3
from time import sleep


class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak_es(self, audio):
        """

        :param audio:
        :return:audio

        """
        es_voice_id = "com.apple.speech.synthesis.voice.monica"
        self.engine.setProperty('voice', es_voice_id)
        self.engine.setProperty('volume', 0.9)
        self.engine.say(audio)
        self.engine.runAndWait()
        return audio

    def speak_en(self, audio):
        """

        :param audio:
        :return:audio

        """
        en_voice_id = 'com.apple.speech.synthesis.voice.Victoria'
        self.engine.setProperty('voice', en_voice_id)
        self.engine.say(audio)
        self.engine.runAndWait()
        return audio


class Assistant(Voice):
    def __init__(self, text):
        super().__init__()
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)

    def recognize_voice(self, y=Voice()):
        with self.mic as source:
            print('listening....')
            # listen the audio via source
            self.r.adjust_for_ambient_noise(source, duration=0.2)
            voice = self.r.listen(source)
            try:
                # define the input language (English)
                result = self.r.recognize_google(voice, language='en-US')
                print(result)
                return result
            except sr.RequestError:
                y.speak_en('check your internet connection')
            except sr.UnknownValueError:
                y.speak_en('I do not get that')
                return None


sleep(1)
