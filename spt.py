import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3

# initialize the microphone of the computer
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

# initialize text to speech(voice)
engine = pyttsx3.init()
voices = engine.getProperty('voices')


def speak_es(audio):
    """
    Spanish voice
    :param audio:
    :return: string
    """

    es_voice_id = "com.apple.speech.synthesis.voice.monica"
    engine.setProperty('voice', es_voice_id)
    engine.say(audio)
    engine.runAndWait()


def speak_de(audio):
    """
    German voice
    :param audio:
    :return: string
    """
    de_voice_id = "com.apple.speech.synthesis.voice.anna"
    engine.setProperty('voice', de_voice_id)
    engine.say(audio)
    engine.runAndWait()


with mic as source:
    # Speak the assistant with the Spanish Voice
    speak_es('Hola, dime lo que quieres traducir')
    # listen the audio via source
    r.adjust_for_ambient_noise(source, 5)
    r.pause_threshold = 1
    audio = r.listen(source)
    # define the input language (Spanish)
    result = r.recognize_google(audio, language='es')
    speak_es('quieres traducir: ' + result + 'en aleman')
    # initialize the translator
    p = google_translator()
    k = p.translate(result, lang_tgt='de')
    # German  Voice
    speak_de(k)

