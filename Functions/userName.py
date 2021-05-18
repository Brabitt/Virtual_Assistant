from SPT.spt import Assistant, Voice


class User(Assistant, Voice):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def username(self, voices=Voice(), x=Assistant()):
        print(voices.speak_en('who you are'))
        self.name = x.recognize_voice()
        print(voices.speak_en('welcome mister' + str(self.name)))
        return None
