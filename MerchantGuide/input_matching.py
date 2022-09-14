import re

from MerchantGuide.utils import words_in_dict, words_to_roman, is_valid
from MerchantGuide.resources import Resource

def set_symbol(input, dict):
    word, roman_sym = re.split("\sis\s", input)
    dict[word] = roman_sym
    return dict

def get_credits(input, word_dict):
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
        # check if the roman number is valid
        # convert roman number into intergalactic
        validation, num = is_valid(roman_num)
        if validation:
            new_Resource = Resource(resource, int(total_credits)/num)
            print(new_Resource.name, new_Resource.credits)
    return new_Resource.name, new_Resource.credits