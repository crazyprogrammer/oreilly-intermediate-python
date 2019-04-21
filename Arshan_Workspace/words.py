# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:19:55 2019

@author: sudachar
"""

import scrabble

#Find the uu or UU text from the file
# print all words containing "uu"

for word in scrabble.wordlist : 
    if 'uu' in word :
        print (word)