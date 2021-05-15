from SPT.spt import Assistant, Voice
import datetime
import webbrowser
from google_trans_new import google_translator

x = Assistant()
assistant = x.recognize_voice()
voices = Voice()

# we create a dictionary with lists in which
# we add expressions for the wizard to respond to us
term = {'translator': ['translator', 'want to translate']}
t = (term["translator"])

if __name__ == '__main__':
    if 'ok' in assistant:
        voices.speak_en('works!!')
    elif 'what time is it' in assistant:
        hour = datetime.datetime.now().hour
        print(hour)
        voices.speak_en("Sir, the time is" + str(hour))
    elif 'search' in assistant:
        print(voices.speak_en('tell what do you want to search '))
        assistant = x.recognize_voice()
        url = 'https://google.com/search?q=' + assistant
        webbrowser.open(url)
        print(voices.speak_en('this is what a found for ' + assistant))
    elif 'music' in assistant:
        voices.speak_en('tell what do you want to search on youtube ')
        assistant = x.recognize_voice()
        url = 'https://www.youtube.com/results?search_query=' + assistant
        webbrowser.open(url)
    elif assistant in t[0:2]:
        translator = google_translator()
        print(voices.speak_en('what do you want to translate'))
        assistant = x.recognize_voice()
        t = translator.translate(assistant, lang_tgt='es')
        voices.speak_es(t)





