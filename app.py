from SPT.spt import Assistant
from SPT.terms import translator, time, google, youtube
from Functions.translator import Translator
from Functions.search import Search
from Functions.time import Time


while True:

    x = Assistant()
    assistant = x.recognize_voice()
    if __name__ == '__main__':
        if assistant in translator:
            x = Translator()
            x.Spanish()

        elif assistant in time:
            z = Time()
            z.Hour()

        elif assistant in google:
            y = Search()
            y.search_google()

        elif assistant in youtube:
            h = Search()
            h.search_youtube()

        else:
            if 'exit' in assistant:
                break
