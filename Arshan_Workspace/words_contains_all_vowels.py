# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:38:34 2019

@author: sudachar
"""

import scrabble

vowels = 'aeiou'

def has_all_vowels(word) : 
    for vowel in vowels : 
        if vowel in word :
            return False
        return True
    
    
for word in scrabble.wordlist : 
    if has_all_vowels : 
        print (word)