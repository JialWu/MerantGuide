import re

def words_in_dict(words, word_dict):
    if all(key in word_dict for key in words):
        return True
    else: 
        print("I have no idea what are you talking about")
        print(word_dict, words)
        return False
    
def words_to_roman(words, word_dict):
    roman_str = ""
    for word in words:
        roman_str += word_dict.get(word)
    return roman_str

def roman_to_credits(roman_num):
    sub_rule = {
        "I": ["V", "X"],
        "X": ["L", "C"],
        "C": ["D", "M"]
    }
    sym_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # I ,X, C, M cannot repeat more than 3 times in succession
    if re.search("I{4}|X{4}|C{4}|M{4}", roman_num): return False
    # V, L, D never repeat
    if re.search("(.*V.*V)|(.*L.*L)|(.*D.*D)", roman_num): return False
    # view the roman number in reverse order for better understand
    roman_num = roman_num[::-1]
    max_sym = roman_num[0]
    num_small_sym = 0
    credits = 0
    for i in range(len(roman_num)):
        if sym_value.get(roman_num[i]) >= sym_value.get(max_sym):
            # it is valid if the latter one is larger than or equall to the current
            # update the maximum number, number of small value and credits
            max_sym = roman_num[i]
            num_small_sym = 0
            credits += sym_value.get(roman_num[i])
        else:
            num_small_sym += 1
            if num_small_sym > 1: return False
            # if it is smaller, the validation of minuend needs to be check
            if any(max_sym in sym for sym in sub_rule.get(roman_num[i])): 
                credits -= sym_value.get(roman_num[i])
            else: 
                return False
        print(max_sym, sym_value.get(max_sym), num_small_sym)
    return credits