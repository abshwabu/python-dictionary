import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def dictionary(word):
    if word in data.keys():
        return data[word]
    else:
        return 'Please cheak your spealing'


word = input('Enter a word: ')

print(dictionary(word))