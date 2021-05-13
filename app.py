from spt import Assistant, Voice
import datetime
import webbrowser

x = Assistant()
assistant = x.recognize_voice()
voices = Voice()

if __name__ == '__main__':
    if 'ok' in assistant:
        voices.speak_en('works!!')
    elif 'what time is it' in assistant:
        hour = datetime.datetime.now().hour
        voices.speak_en("Sir, the time is" + str(hour))
    elif 'search' in assistant:
        voices.speak_en('tell what do you want to search ')
        assistant = x.recognize_voice()
        url = 'https://google.com/search?q=' + assistant
        webbrowser.open(url)
    elif 'music' in assistant:
        voices.speak_en('tell what do you want to search on youtube ')
        assistant = x.recognize_voice()
        url = 'https://www.youtube.com/results?search_query=' + assistant
        webbrowser.open(url)




