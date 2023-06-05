import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def dictionary(word):
    if word in data.keys():
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        conferm = input(f'Do you mean {get_close_matches(word,data.keys())[0]}?\ny for yes or n for no: ')
        conferm = conferm.lower()
        if conferm == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        else:
            return 'pleade check your spealing and try again'
    else:
        return 'Please cheak your spealing'

while True:
    word = input('Enter a word: ')
    if word == '\\end':
        break
    else:
        output = dictionary(word)
        if type(output) == list:
            for op in output:
                print(op)
        else:
            print(output)