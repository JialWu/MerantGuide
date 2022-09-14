def words_in_dict(words, word_dict):
    if all(key in word_dict for key in words):
        return True
    else: 
        print("I have no idea what are you talking about")
        return False
    
def words_to_roman(words, word_dict):
    roman_str = ""
    for word in words:
        roman_str += word_dict.get(word)
    return roman_str