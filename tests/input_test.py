import unittest

from MerchantGuide import input_matching

class TestInput(unittest.TestCase):
    def test_set_symbol(self):
        input = "glob is I"
        self.assertEqual(input_matching.set_symbol(input, {}), {"glob": "I"})
        
    def test_calculate_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        input = "glob glob Silver is 34 Credits"
        self.assertEqual(input_matching.get_credits(input, word_to_roman))

        
if __name__ == '__main__':
    unittest.main()