def words_in_dic(words, word_dict):
    if all(key in word_dict for key in words):
        return True
    else: 
        raise Exception("Sorry, no numbers below zero")