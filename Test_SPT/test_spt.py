import unittest
import pyttsx3
from SPT.spt import Assistant, Voice
import speech_recognition as sr


class Test_Assistant(unittest.TestCase, Assistant):

    def test_recognize_voice(self, y=Voice()):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone(device_index=0)
        with self.mic as source:
            print('listening....')
            # listen the audio via source
            self.r.adjust_for_ambient_noise(source, duration=0.2)
            voice = self.r.listen(source)
            try:
                # define the input language (English)
                result = self.r.recognize_google(voice, language='en-US')
                print(result)
                # checking if the result is True
                self.assertTrue(result)
                return result
            except sr.RequestError:
                # checking if it catches errors
                if self.assertRaises(sr.RequestError):
                    print('connection error caught ')
                    print(y.speak_en('check your internet connection'))
                return None
            except sr.UnknownValueError:
                # checking if it catches errors
                if self.assertRaises(sr.UnknownValueError):
                    print('error caught')
                    print(y.speak_en('I do not get that'))
                return None


class test_Voice(unittest.TestCase, Voice):
    # checking if the audio parameter is executed correctly by the pyttsx3 interpreter
    def test_speaks(self, audio='hello'):
        self.engine = pyttsx3.init()
        es_voice_id = "com.apple.speech.synthesis.voice.monica"
        self.engine.setProperty('voice', es_voice_id)
        self.engine.setProperty('volume', 0.9)
        self.engine.say(audio)
        self.engine.runAndWait()
        # checking if the parameter audio is True
        if self.assertTrue(audio):
            print('audio = True')
        else:
            print('audio = False')
        return audio


if __name__ == '__main__':
    unittest.main()
