import datetime

import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3
from time import sleep


# initialize the microphone of the computer
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

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


def recognize_voice():
    with mic as source:
        # Speak the assistant with the Spanish Voice
        speak_en('hello, how can I help you?')
        audio_data = ''
        # listen the audio via source
        r.adjust_for_ambient_noise(source)
        voice = r.listen(source)
        try:
            # define the input language (Spanish)
            audio_data = r.recognize_google(voice, language='en-in')
            print(audio_data)
            if 'yes' in audio_data:
                speak_en('works fine!!')
        except sr.RequestError:
            speak_en('check your internet conetion')
        except sr.UnknownValueError:
            speak_en('i dont get  that')
        return audio_data.lower()


sleep(1)
if __name__ == '__main__':
    recognize_voice()
