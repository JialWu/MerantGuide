import re

from utils import words_in_dict, words_to_roman, roman_to_credits
from resources import Resource

def set_symbol(input, dict):
    word, roman_sym = re.split("\sis\s", input)
    dict[word] = roman_sym

def get_credits(input, word_dict, resource_dic):
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
        print(credits)
        # TODO: when credits is 0
        
        resource_dic.add_resource(Resource(resource, int(total_credits)/credits))
        
def convert_to_credits(input, word_dict):
    _, words = re.split("\sis\s", input)
    words, _ = re.split("[?]", words)
    print(words)
    word_sequence = words.split()
    if words_in_dict(word_sequence, word_dict):
        # convert the words to roman numerals
        roman_num = words_to_roman(word_sequence, word_dict)
        credits = roman_to_credits(roman_num)
        print(words + "is " + str(credits))
        
def calculate_credits(input, word_dict, resource_dic):
    _, words = re.split("\sis\s", input)
    words, _ = re.split("[?]", words)
    
    [resource] = re.findall("[A-Z]\w*", words)
    
    # find all words need to be converted to roman number
    word_sequence = words.split()
    word_sequence.remove(resource)
    
    res_credits = 0
    # my_filter_iter = filter(lambda x: x.name == resource, resource_dic)
    for res in resource_dic.get_resource():
        print(res.name, res.credits)
        if res.name == resource:
            res_credits = res.credits
            print(res.name, res.credits)
    print(res_credits)
            
    if words_in_dict(word_sequence, word_dict):
        # convert the words to roman numerals
        roman_num = words_to_roman(word_sequence, word_dict)
        # check if the roman number is valid
        # convert roman number into intergalactic
        credits = roman_to_credits(roman_num)
        print(credits)
        print(words + "is " + str(credits * res_credits) + " Credits")
    