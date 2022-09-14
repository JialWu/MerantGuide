import re

from resources import Resource
from utils import words_in_dic

def set_roman(input, dict):
    word, roman_num = re.split("\sis\s", input)
    dict[word] = roman_num
    return dict
def calculate_credits(input, word_dict):
    words_and_resource, credits = re.split("\sis\s", input)
    # find the resource and its credits
    [resource] = re.findall("[A-Z]\w*", words_and_resource)
    [credits] = re.findall("\d+", credits)
    new_Resource = Resource(resource, int(credits))
    print(new_Resource.name, new_Resource.credits)
    # find all words need to be converted to roman number
    words = words_and_resource.split()
    words.remove(resource)
    # TODO: check if each word exists in the word_to_roman dictionary 
    #       words_in_dict(words, word_dict)
    
    # TODO: convert the words to roman number 
    #       words_to_roman(words, word_dict)
    
    # TODO: check if the roman number is valid
    #       is_valid(roman_num)
    return words, new_Resource
def main():
    # data = sys.stdin.read()
    # print(data)
    user_input = []
    word_to_roman = {}
    while True:
        user_input = input()
        if user_input == "":
            break
        else:
            switch = {
                0: set_roman,
                1: calculate_credits
            }
            if re.search(".*is\s*(I|V|X|L|C|D|M)$", user_input): input_maching = 0
            elif re.search("(.*)\s*[A-Z](.*)\s*(is)\s*(\d+)\s*(Credits)", user_input): input_maching = 1
            elif re.search("how\s*much\s*is.*", user_input): input_maching = 2 
            elif re.search("how\s*many\s*Credits\s*is\s*.*", user_input): input_maching = 3
            else: input_maching = 4
            
            if input_maching in switch.keys():
                output = switch[input_maching](user_input, word_to_roman)
                print(input_maching, output)

if __name__=="__main__":
    main()