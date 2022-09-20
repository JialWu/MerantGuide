import re

from MerchantGuide.input_matching import set_symbol, get_credits, convert_to_credits, calculate_credits
from MerchantGuide.resources import Resource_List
    
def main():
    user_input = []
    word_to_roman = {}
    resource_list = Resource_List()
    
    while True:
        user_input = input()
        if user_input == "quit":
            break
        else:
            switch = {
                0: set_symbol,
                1: get_credits,
                2: convert_to_credits,
                3: calculate_credits 
            }
            
            if re.search(".*is\s*(I|V|X|L|C|D|M)$", user_input): input_maching = 0
            elif re.search("(.*)\s*[A-Z](.*)\s*(is)\s*(\d+)\s*(Credits)", user_input): input_maching = 1
            elif re.search("^how\s*much\s*is.*", user_input): input_maching = 2 
            elif re.search("^how\s*many\s*Credits\s*is\s*.*", user_input): input_maching = 3
            else: input_maching = 4
            
            # invalid input queries handlings
            try:
                if input_maching == 2:
                    words, credicts = switch[input_maching](user_input, word_to_roman, resource_list)
                    print(words + " is " + str(credicts))
                elif input_maching == 3:
                    words_and_resource, result = switch[input_maching](user_input, word_to_roman, resource_list)
                    print(words_and_resource + " is " + str(result) + " Credits")
                else:
                    switch[input_maching](user_input, word_to_roman, resource_list)
            except KeyError:
                print("I have no idea what are you talking about")
            except Exception as e:
                print(e)
            
            # check validation
            # if re.search("(I|V|X|L|C|D|M)*", user_input): print(is_valid(user_input))

if __name__=="__main__":
    main()
