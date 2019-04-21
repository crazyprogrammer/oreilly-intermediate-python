# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:26:16 2019

@author: sudachar
"""

# Letters that never appear double

import scrabble
import string

for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist :
        if letter * 2 in word :
            exists = True
            break
    
    if not exists : 
        print('There are no words in which they are doubled in any word for : %s' % letter )