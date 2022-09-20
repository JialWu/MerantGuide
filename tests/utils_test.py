import unittest

from MerchantGuide.utils import words_in_dict, words_to_roman, roman_to_credits

class TestUtils(unittest.TestCase):
    def test_words_in_dict(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        
        words = ["prok", "tegj"]
        self.assertEqual(words_in_dict(words, word_to_roman), True)
        
        words = ["prok", "pis"]
        self.assertEqual(words_in_dict(words, word_to_roman), False)
    
    def test_words_to_roman(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        
        words = ["pish", "tegj", "glob", "glob"]
        self.assertEqual(words_to_roman(words, word_to_roman), "XLII")
        
        words = ["grob"]
        with self.assertRaises(Exception):
            words_to_roman(words, word_to_roman)
            
        words = ["prok", "pis"]
        with self.assertRaises(Exception):
            words_to_roman(words, word_to_roman)
            
    def test_roman_to_credits(self):
        roman_num = "XLII"
        self.assertEqual(roman_to_credits(roman_num), 42)
        
        roman_num = "MCMXLIV"
        self.assertEqual(roman_to_credits(roman_num), 1944)
        
        roman_num = "XXXXI"
        with self.assertRaises(Exception):
            roman_to_credits(roman_num)
            
        roman_num = "IVV"
        with self.assertRaises(Exception):
            roman_to_credits(roman_num)
        
        roman_num = "VX"
        with self.assertRaises(Exception):
            roman_to_credits(roman_num)
            
        roman_num = "IIX"
        with self.assertRaises(Exception):
            roman_to_credits(roman_num)
            

if __name__ == '__main__':
    unittest.main()
        
        