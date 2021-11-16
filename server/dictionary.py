import json;


class Dictionary():
    def __init__(self):
        with open("words_dictionary.json") as dictionary_file:
            self.dictionary = json.load(dictionary_file)

    def is_word(self, word):
        return word in self.dictionary
        
