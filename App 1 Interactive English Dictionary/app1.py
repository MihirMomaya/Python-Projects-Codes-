import json
from difflib import get_close_matches

data=json.load(open('data.json'))

def translate(word):
    word=word.lower()
    if word in data:
            return data[word]
    elif word.title() in data:
            return data[word.title()]
    elif word.upper() in data:
            return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        yn=input('did you mean %s instead ? Enter Y for Y , N for no :' %get_close_matches(word,data.keys(),cutoff=0.8)[0])
        if yn =='Y':
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif yn=='N':
            return "The word doesn't exist. Please double check it. "
        else :
            'We didnt understand your entry .'
    else :
        return "The word doesn't exist. Please double check it. "

word=input("Enter a word ")
output=translate(word)

if type(output) == list:
    for a in output:
        print(a)
else:
    print(output)