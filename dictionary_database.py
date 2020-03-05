# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:28:13 2019

@author: Sayantan
"""

import mysql.connector
from difflib import get_close_matches

word = input ("Enter Word: ")

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"                              
)
cursor = con.cursor()
query_words = cursor.execute("select distinct(Expression) from Dictionary")
word_list_inter = cursor.fetchall()
word_list = []
for each_word in word_list_inter:
    word_list.append(each_word[0])
query_main = cursor.execute("select * from Dictionary where Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for item in results:
        print(item[1])
else:
    if len(get_close_matches(word,word_list,cutoff=0.8)) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(word,word_list,cutoff=0.8)[0])
        if yn.lower() == "y":
            query_near = cursor.execute("select * from Dictionary where Expression = '%s'" % get_close_matches(word,word_list,cutoff=0.8)[0])
            results_near = cursor.fetchall()
            for item_near in results_near:
                print(item_near[1])
        elif yn.lower() == "n":
             print("The word doesn't exist. Please double check on it.")
        else:
            print("We didn't understand your input")
    else:
        print("No such word found..!!")
        