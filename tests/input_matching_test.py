import unittest

import sys
from contextlib import contextmanager
from io import StringIO

from MerchantGuide import input_matching
from MerchantGuide.resources import Resource_List, Resource

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestInput(unittest.TestCase):
    def test_set_symbol(self):
        input = "glob is I"
        dict = {}
        input_matching.set_symbol(input, dict, None)
        self.assertEqual(dict, {"glob": "I"})
        
    def test_get_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        resource_list = Resource_List()
        input = "glob glob Silver is 34 Credits"
        input_matching.get_credits(input, word_to_roman, resource_list)

        for resource in resource_list.get_resource():
            self.assertEqual(resource.name, "Silver")
            self.assertEqual(resource.credits, 17)
            
    def test_convert_to_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        input = "how much is pish tegj glob glob ?"
        with captured_output() as (out, err):
            input_matching.convert_to_credits(input, word_to_roman, resource_list=None)
        output = out.getvalue().strip()
        self.assertEqual(output, 'pish tegj glob glob is 42')
        
    def test_calculate_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        resource_list = Resource_List()
        resource_list.add_resource(Resource("Silver", 17))
        input = "how many Credits is glob prok Silver ?"
        with captured_output() as (out, err):
            input_matching.calculate_credits(input, word_to_roman, resource_list)
        output = out.getvalue().strip()
        self.assertEqual(output, 'glob prok Silver is 68 Credits')
        
if __name__ == '__main__':
    unittest.main()