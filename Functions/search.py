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
        url = 'https://google.com/search?q=' + assistant
        new_url = self.open(url)
        print(voices.speak_en('this is what a found for ' + assistant))
        return new_url

    # method for search on google
    def search_youtube(self, voices=Voice(), x=Assistant()):
        print(voices.speak_en('tell what do you want to search on youtube '))
        assistant = x.recognize_voice()
        url = 'https://www.youtube.com/results?search_query=' + assistant
        new_url = self.open(url)
        print(voices.speak_en('this is what a found for ' + assistant))
        return new_url
