from SPT.spt import Assistant, Voice
import webbrowser as wb


class Search(Assistant, Voice):
    def __init__(self):
        super().__init__()
        self.open = wb.open

    # method for search on google
    def search_google(self, voices=Voice(), x=Assistant()):
        print(voices.speak_en('tell what do you want to search '))
        assistant = x.recognize_voice()
        if assistant:
            url = 'https://google.com/search?q=' + str(assistant)
            new_url = self.open(url)
            print(voices.speak_en('this is what a found for ' + str(assistant)))
            return new_url
        else:
            return None

    # method for search on YouTube
    def search_youtube(self, voices=Voice(), x=Assistant()):
        print(voices.speak_en('tell what do you want to search on youtube '))
        assistant = x.recognize_voice()
        if assistant:
            url = 'https://www.youtube.com/results?search_query=' + str(assistant)
            new_url = self.open(url)
            print(voices.speak_en('this is what a found for ' + str(assistant)))
            return new_url
        else:
            return None
