import speech_recognition as sr
from google_trans_new import google_translator
import pyttsx3

# initialize the microphone of the computer
r = sr.Recognizer()
mic = sr.Microphone(device_index=0)

# initialize text to speech(voice)
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Spanish Voice
es_voice_id = "com.apple.speech.synthesis.voice.monica"
engine.setProperty('voice', es_voice_id)

with mic as source:
    # Speak the assistant with the Spanish Voice
    engine.say('Hola, dime lo que quieres traducir')
    engine.runAndWait()
    # listen the audio via source
    r.adjust_for_ambient_noise(source)
    r.pause_threshold = 1
    audio = r.listen(source)
    # define the input language (Spanish)
    result = r.recognize_google(audio, language='es')
    engine.say('quieres traducir: ' + result + 'en aleman')
    engine.runAndWait()
    # initialize the translator
    p = google_translator()
    k = p.translate(result, lang_tgt='de')
    # German  Voice
    de_voice_id = "com.apple.speech.synthesis.voice.anna"
    engine.setProperty('voice', de_voice_id)
    engine.say(k)
    engine.runAndWait()
