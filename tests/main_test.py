import unittest

import MerchantGuide.merchantGuide as merchantGuide

class TestMain(unittest.TestCase):
    def test_main(self):
        test_input = ["glob is I",
                      "prok is V",
                      "pish is X",
                      "tegj is L",
                      "glob glob Silver is 34 Credits",
                      "glob prok Gold is 57800 Credits",
                      "pish pish Iron is 3910 Credits",
                      "how much is pish tegj glob glob ?",
                      "how many Credits is glob prok Silver ?",
                      "how many Credits is glob prok Gold ?",
                      "how many Credits is glob prok Iron ?",
                      "how much wood could a woodchunk chunk if a woodchunk could chunk wood ?",
                      "quit"]
        input_values = test_input
        output = []
        
        def mock_input():
            return input_values.pop(0)
        
        merchantGuide.input = mock_input
        merchantGuide.print = lambda s : output.append(s)
        merchantGuide.main()
        
        assert output == ["pish tegj glob glob is 42",
                          "glob prok Silver is 68 Credits",
                          "glob prok Gold is 57800 Credits",
                          "glob prok Iron is 782 Credits",
                          "I have no idea what are you talking about"]
        
if __name__ == '__main__':
    unittest.main()