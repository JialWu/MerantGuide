import re

def set_roman(input, dic):
    word, roman_num = re.split("\sis\s", input)
    dic[word] = roman_num
    return dic
def calculate_credits(input, dic):
    resources = re.findall("[A-Z]\w*", input)
    return resources
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
            if re.search(".*is\s*I|V|X|L|C|D|M$", user_input): input_maching = 0
            elif re.search(".*is\s*\d+\s*Credits", user_input): input_maching = 1
            elif re.search("how\s*much\s*is.*", user_input): input_maching = 2 
            elif re.search("how\s*many\s*Credits\s*is\s*.*", user_input): input_maching = 3
            else: input_maching = 4
            #output = switch[input_maching](user_input, word_to_roman)
            print(input_maching)

if __name__=="__main__":
    main()