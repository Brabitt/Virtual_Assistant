import unittest
from Functions.search import Search
import webbrowser as wb
from SPT.spt import Voice, Assistant


class test_Search_Google(unittest.TestCase, Search):

    def test_search_google_assert(self):
        self.assertTrue(test_Search_Google)
        print('testing the search functions....')

    def test_search_google(self, voices=Voice(), x=Assistant()):
        self.open = wb.open
        print(voices.speak_en('tell what do you want to search '))
        assistant = x.recognize_voice()
        url = 'https://google.com/search?q=' + assistant
        new_url = self.open(url)
        print(voices.speak_en('this is what a found for ' + assistant))
        return new_url

    def test_search_youtube(self, voices=Voice(), x=Assistant()):
        self.open = wb.open
        print(voices.speak_en('tell what do you want to search on youtube '))
        assistant = x.recognize_voice()
        url = 'https://www.youtube.com/results?search_query=' + assistant
        new_url = self.open(url)
        print(voices.speak_en('this is what a found for ' + assistant))
        return new_url


if __name__ == '__main__':
    unittest.main()
