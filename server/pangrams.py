import json
from random import randint

pangrams = {}


def is_pangram(word):
    if len(set(word)) == 7 and 's' not in word:
        return True
    else:
        return False

def get_pangram():
    
    with open("words_dictionary.json") as json_file:
        words = json.load(json_file)

        for word in words:
            if is_pangram(word):
                pangrams[word] = ""

    with open("pangrams.json", "w") as pangram_file:
        json.dump(pangrams, pangram_file)
        
    # Pick a random pangram
    rand_num = randint(0, len(pangrams-1))
    random_pangram = list(pangrams.keys())[rand_num]
    return random_pangram
    
#print(random_pangram)
#print(set(random_pangram))  # dont need to return the set
