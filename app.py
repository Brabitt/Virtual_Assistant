from SPT.spt import Assistant
from SPT.terms import translator, time, google, youtube, exit, virtual_assistant
from Functions.translator import Translator
from Functions.search import Search
from Functions.time import Time
from Functions.userName import User


u = User('')
u.username()

while True:

    x = Assistant()
    assistant = x.recognize_voice()
    if __name__ == '__main__':
        if assistant in translator:
            interpreter = Translator()
            interpreter.Spanish()

        elif assistant in time:
            clock = Time()
            clock.Hour()

        elif assistant in google:
            search_google = Search()
            search_google.search_google()

        elif assistant in youtube:
            search_youtube = Search()
            search_youtube.search_youtube()

        elif assistant in virtual_assistant:
            u = User('')
            u.username()

        elif assistant in exit:
            break
