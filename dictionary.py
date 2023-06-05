import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def dictionary(word):
    if word in data.keys():
        return data[word]
    elif len(word,get_close_matches(data.keys())) > 0:
        
        return get_close_matches(data.keys()[0])
    else:
        return 'Please cheak your spealing'


word = input('Enter a word: ')
output = dictionary(word)
if type(output) == list:
    for op in output:
        print(op)
else:
    print(output)