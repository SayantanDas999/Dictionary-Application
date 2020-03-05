# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:28:13 2019

@author: Sayantan
"""

import json
from difflib import get_close_matches

def word_dict():
    word = input("Enter Word: ") 
    data = json.load(open("data.json"))
    if word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(word,data.keys(),cutoff=0.8)[0])
        if yn.lower() == "y":
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif yn.lower() == "n":
             return "The word doesn't exist. Please double check on it."
        else:
            return "We didn't understand your input"
    else:
        return "The word doesn't exist. Please double check on it."

output = word_dict()

if isinstance(output, list):
    for item in output:
        print(item)
else:
    print(output)
