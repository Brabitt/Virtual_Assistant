import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3
from time import sleep
import datetime


# initialize text to speech(voice)
engine = pyttsx3.init()


def speak_es(audio_data):
    """
    Spanish voice
    :param audio_data:
    :return: string
    """
    es_voice_id = "com.apple.speech.synthesis.voice.monica"
    engine.setProperty('voice', es_voice_id)
    engine.say(audio_data)
    engine.runAndWait()


def speak_de(audio_data):
    """
    German voice
    :param audio_data:
    :return: string
    """
    de_voice_id = "com.apple.speech.synthesis.voice.anna"
    engine.setProperty('voice', de_voice_id)
    engine.say(audio_data)
    engine.runAndWait()


def speak_en(audio_data):
    en_voice_id = 'com.apple.speech.synthesis.voice.Victoria'
    engine.setProperty('voice', en_voice_id)
    engine.say(audio_data)
    engine.runAndWait()


class Assistant:
    def __init__(self, r, mic):
        self.r = r
        self.mic = mic

    def recognize_voice(self):
        with self.mic as source:
            print('listening....')
            # listen the audio via source
            self.r.adjust_for_ambient_noise(source)
            voice = self.r.listen(source)
            try:
                # define the input language (English)
                audio_data = self.r.recognize_google(voice, language='en-in')
                print(audio_data)
                if 'what time is it' in audio_data:
                    print(datetime.datetime.now())
            except sr.RequestError:
                speak_en('check your internet connection')
            except sr.UnknownValueError:
                speak_en('I do not get that')
            return audio_data.lower()


sleep(1)
if __name__ == '__main__':
    # initialize the microphone of the computer
    x = Assistant(sr.Recognizer(), sr.Microphone(device_index=0))
    print(x.recognize_voice())
