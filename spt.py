import speech_recognition as sr
import pyttsx3
from time import sleep
import datetime


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
    def __init__(self):
        super().__init__()
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)

    def recognize_voice(self, y=Voice()):
        with self.mic as source:
            print('listening....')
            # listen the audio via source
            self.r.adjust_for_ambient_noise(source)
            self.r.dynamic_energy_threshold = 3000
            voice = self.r.listen(source, timeout=5.0)
            try:

                # define the input language (English)
                audio_data = self.r.recognize_google(voice, language='en-in')
                print(audio_data)
                if 'what time is it' in audio_data:
                    y.speak_en(str(datetime.datetime.now()))
            except sr.RequestError:
                y.speak_en('check your internet connection')
            except sr.UnknownValueError:
                y.speak_en('I do not get that')


sleep(1)
if __name__ == '__main__':
    # initialize the microphone of the computer
    x = Assistant()
    x.recognize_voice()
