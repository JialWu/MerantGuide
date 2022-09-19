import unittest
from unittest.mock import patch

import sys
from contextlib import contextmanager
from io import StringIO

from MerchantGuide import input_matching
from MerchantGuide.resources import Resource_List

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
        
    def test_calculate_credits(self):
        word_to_roman = {
            "glob": "I",
            "prok": "V",
            "pish": "X",
            "tegj": "L"
        }
        resource_list = Resource_List()
        input = "ndkl ndjd Silver is 34 Credits"
        with captured_output() as (out, err):
            input_matching.get_credits(input, word_to_roman, resource_list)
        # This can go inside or outside the `with` block
        output = out.getvalue().strip()
        self.assertEqual(output, 'I have no idea what are you talking about')
        #for resource in resource_list.get_resource():
        #     print(resource)