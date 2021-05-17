from datetime import datetime
from SPT.spt import Assistant, Voice


class Time(Assistant, Voice):

    def __init__(self):
        super().__init__()
        self.hour = datetime.now()

    def Hour(self, voices=Voice()):
        print(self.hour)
        voices.speak_en("Sir, the time is" + str(self.hour))
        return self.hour
