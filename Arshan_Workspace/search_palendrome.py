# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 17:43:00 2019

@author: sudachar
"""
import scrabble

longest_palindrome = ''

for word in scrabble.wordlist : 
    is_palindrome = True
    for index in range(len(word)) :
        if word[index] != word[-(index + 1)]:
            is_palindrome = False
    
    if is_palindrome and len(word) > len(longest_palindrome) : 
        longest_palindrome = word

print(longest_palindrome)