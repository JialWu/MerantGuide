from lib2to3.pytree import convert
import re

from utils import set_symbol, get_credits
    
def main():
    user_input = []
    word_to_roman = {}
    while True:
        user_input = input()
        if user_input == "":
            break
        else:
            switch = {
                0: set_symbol,
                1: get_credits,
                #2: convert_to_credits,
                #3: calculate_credits 
            }
            if re.search(".*is\s*(I|V|X|L|C|D|M)$", user_input): input_maching = 0
            elif re.search("(.*)\s*[A-Z](.*)\s*(is)\s*(\d+)\s*(Credits)", user_input): input_maching = 1
            elif re.search("how\s*much\s*is.*", user_input): input_maching = 2 
            elif re.search("how\s*many\s*Credits\s*is\s*.*", user_input): input_maching = 3
            else: input_maching = 4
            
            if input_maching in switch.keys():
                output = switch[input_maching](user_input, word_to_roman)
                print(input_maching, output)
            
            # check validation
            # if re.search("(I|V|X|L|C|D|M)*", user_input): print(is_valid(user_input))

if __name__=="__main__":
    main()