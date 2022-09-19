import re

from .utils import words_in_dict, resource_in_list, words_to_roman, roman_to_credits
from .resources import Resource
from .error_handler import invalid_queries

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
        # check if the roman number is valid
        # convert roman number into intergalactic
        credits = roman_to_credits(roman_num)
        # TODO: when credits is 0
        try:
            credits = int(total_credits)/credits
        except:
            invalid_queries()
        else:
            if int(total_credits) % credits == 0:
                credits = int(credits)
            resource_list.add_resource(Resource(resource, credits))
    else: invalid_queries()
        
def convert_to_credits(input, word_dict, resource_list=None):
    _, words = re.split("\sis\s", input)
    words, _ = re.split("[?]", words)
    word_sequence = words.split()
    if words_in_dict(word_sequence, word_dict):
        # convert the words to roman numerals
        roman_num = words_to_roman(word_sequence, word_dict)
        credits = roman_to_credits(roman_num)
        print(words + "is " + str(credits))
    else: invalid_queries()
        
def calculate_credits(input, word_dict, resource_list):
    _, words = re.split("\sis\s", input)
    words, _ = re.split("[?]", words)
    
    [resource] = re.findall("[A-Z]\w*", words)
    
    # find all words need to be converted to roman number
    word_sequence = words.split()
    word_sequence.remove(resource)
    
    res_credits = 0
    if words_in_dict(word_sequence, word_dict) and resource_in_list(resource, resource_list):
        # get the resource's credits
        for res in resource_list.get_resource():
            if res.name == resource:
                res_credits = res.credits
                break
        # convert the words to roman numerals
        roman_num = words_to_roman(word_sequence, word_dict)
        # check if the roman number is valid
        # convert roman number into intergalactic
        credits = roman_to_credits(roman_num)
        print(words + "is " + str(credits * res_credits) + " Credits")
    else: invalid_queries()