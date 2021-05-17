import unittest
from SPT.spt import Assistant, Voice


class Test_Assistant(unittest.TestCase, Assistant):
    # Test to check if the result is True
    def test_recognize_voice(self):
        self.assertTrue(Assistant.recognize_voice)


class Test_Voice(unittest.TestCase, Assistant):
    # Tests to check if the result is True
    def test_speak_es(self):
        self.assertTrue(Voice.speak_es)

    def test_speak_en(self):
        self.assertTrue(Voice.speak_en)


if __name__ == '__main__':
    unittest.main()
