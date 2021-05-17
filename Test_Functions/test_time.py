import unittest
from SPT.spt import Voice
from Functions.time import Time
from datetime import datetime


class test_Time(unittest.TestCase, Time):
    def test_Hour(self, voices=Voice()):
        self.hour = datetime.now()
        voices.speak_en("Sir, the time is" + str(self.hour))
        return self.hour

    def test_hour_Equal(self):
        self.hour = datetime.now()
        expected = self.hour
        result = expected
        self.assertEqual(expected, result)
