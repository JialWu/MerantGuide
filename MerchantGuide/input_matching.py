import re

from MerchantGuide.utils import words_in_dict, words_to_roman, roman_to_credits

def set_symbol(input, dict, resource_list=None):
    word, roman_sym = re.split("\sis\s", input)
    dict[word] = roman_sym

def get_credits(input, word_dict, resource_list):
    words_and_resource, total_credits = re.split("\sis\s", input)
    # find the resource and its credits
    [resource] = re.findall("[A-Z]\w*", words_and_resource)
    [total_credits] = re.findall("\d+", total_credits)
    
    # find all words need to be converted to roman number
    words = words_and_resource.split()
    words.remove(resource)
    # check if each word exists in the word_to_roman dictionary 
    if words_in_dict(words, word_dict):
        # convert the words to roman numerals
        roman_num = words_to_roman(words, word_dict)
        try:
            # check if the roman number is valid and
            # convert roman number into intergalactic
            credits = roman_to_credits(roman_num)
            res_credits = int(total_credits)/credits
        except: raise
        if int(total_credits) % credits == 0:
            res_credits = int(res_credits)
        resource_list.add_resource(resource, res_credits)
    else: raise Exception("Error in word sequense: some words are not defined with Roman numeral.")
        
def convert_to_credits(input, word_dict, resource_list=None):
    _, words = re.split("\sis\s", input)
    words, _ = re.split("\s*[?]", words)
    word_sequence = words.split()
    if words_in_dict(word_sequence, word_dict):
        # convert the words to roman numerals
        roman_num = words_to_roman(word_sequence, word_dict)
        try:
            # check if the roman number is valid and
            # convert roman number into intergalactic
            credits = roman_to_credits(roman_num)
        except: raise
        return words, credits
    else: raise Exception("Error in word sequense: some words are not defined with Roman numeral.")
        
def calculate_credits(input, word_dict, resource_list):
    _, words_and_resource = re.split("\sis\s", input)
    words_and_resource, _ = re.split("\s*[?]", words_and_resource)
    
    [resource] = re.findall("[A-Z]\w*", words_and_resource)
    
    # find all words need to be converted to roman number
    word_sequence = words_and_resource.split()
    word_sequence.remove(resource)
    
    res_credits = 0
    if words_in_dict(word_sequence, word_dict) and resource_list.resource_in_list(resource):
        # get the resource's credits
        res_credits = resource_list.get_credits(resource)
        # convert the words to roman numerals
        roman_num = words_to_roman(word_sequence, word_dict)
        try:
            # check if the roman number is valid and
            # convert roman number into intergalactic
            credits = roman_to_credits(roman_num)
        except: raise
        if (credits * res_credits) % 1 == 0:
            result = int(credits * res_credits)
        else: result = credits * res_credits
        return words_and_resource, result
    else: raise Exception("Error in word sequense or there is no credit price for resource.")