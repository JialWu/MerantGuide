import re

from input_matching import set_symbol, get_credits, convert_to_credits, calculate_credits
from resources import Resource_List
    
def main():
    user_input = []
    word_to_roman = {}
    resource_dic = Resource_List()
    
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
            if re.search(".*is\s*(I|V|X|L|C|D|M)$", user_input): 
                input_maching = 0
                set_symbol(user_input, word_to_roman)
                print(word_to_roman)
            elif re.search("(.*)\s*[A-Z](.*)\s*(is)\s*(\d+)\s*(Credits)", user_input): 
                input_maching = 1
                get_credits(user_input, word_to_roman, resource_dic)
                for resource in resource_dic.get_resource():
                    print(resource)
            elif re.search("how\s*much\s*is.*", user_input): 
                input_maching = 2 
                convert_to_credits(user_input, word_to_roman)
            elif re.search("how\s*many\s*Credits\s*is\s*.*", user_input): 
                input_maching = 3
                calculate_credits(user_input, word_to_roman, resource_dic)
            else: input_maching = 4
            
            #if input_maching in switch.keys():
            #    output = switch[input_maching](user_input, word_to_roman)
            #    print(input_maching, output)
            
            # check validation
            # if re.search("(I|V|X|L|C|D|M)*", user_input): print(is_valid(user_input))

if __name__=="__main__":
    main()