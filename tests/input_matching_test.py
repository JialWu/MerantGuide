import unittest

from MerchantGuide.input_matching import set_symbol, convert_to_credits, get_credits, calculate_credits
from MerchantGuide.resources import Resource_List

class TestInputMatching(unittest.TestCase):
    def test_set_symbol(self):
        word_to_roman = {}
        
        input = "glob is X"
        set_symbol(input, word_to_roman, None)
        self.assertEqual(word_to_roman, {"glob": "X"})
        
        input = "glob is I"
        set_symbol(input, word_to_roman, None)
        self.assertEqual(word_to_roman, {"glob": "I"})
        
        input = "dekn is V"
        set_symbol(input, word_to_roman, None)
        self.assertEqual(word_to_roman, {"glob": "I", "dekn": "V"})
        
    def test_get_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        resource_list = Resource_List()
        input = "glob glob Silver is 34 Credits"
        get_credits(input, word_to_roman, resource_list)
        self.assertEqual(resource_list.resource_in_list("Silver"), True)
        self.assertEqual(resource_list.get_credits("Silver"), 17)
        
        input = "glob glob Silver is 56 Credits"
        get_credits(input, word_to_roman, resource_list)
        self.assertEqual(resource_list.resource_in_list("Silver"), True)
        self.assertEqual(resource_list.get_credits("Silver"), 28)
        
        input = "glos glob Silver is 56 Credits"
        with self.assertRaises(Exception):
            get_credits(input, word_to_roman, resource_list)
            
    def test_convert_to_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        input = "how much is pish tegj glob glob ?"
        self.assertEqual(convert_to_credits(input, word_to_roman, resource_list=None), ("pish tegj glob glob", 42))
        
        input = "how much is qish ?"
        with self.assertRaises(Exception):
            convert_to_credits(input, word_to_roman, resource_list=None)
            
        input = "how much is prok glob glob glob glob?"
        with self.assertRaises(Exception):
            convert_to_credits(input, word_to_roman, resource_list=None)
            
        input = "how much is prok pish prok?"
        with self.assertRaises(Exception):
            convert_to_credits(input, word_to_roman, resource_list=None)
        
        input = "how much is glob tegj?"
        with self.assertRaises(Exception):
            convert_to_credits(input, word_to_roman, resource_list=None)
        
    def test_calculate_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        resource_list = Resource_List()
        resource_list.add_resource("Silver", 17)
        input = "how many Credits is glob prok Silver ?"
        self.assertEqual(calculate_credits(input, word_to_roman, resource_list), ("glob prok Silver", 68))
        
        input = "how many Credits is glof prok Silver ?"
        with self.assertRaises(Exception):
            calculate_credits(input, word_to_roman, resource_list)
            
        input = "how many Credits is glob prok Copper ?"
        with self.assertRaises(Exception):
            calculate_credits(input, word_to_roman, resource_list)
            
        
if __name__ == '__main__':
    unittest.main()