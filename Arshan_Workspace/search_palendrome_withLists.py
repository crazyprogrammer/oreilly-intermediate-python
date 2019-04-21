# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:07:57 2019

@author: sudachar
"""

import scrabble

longest_palindrome = ''

'''
for word in scrabble.wordlist :
    if list(word) == list(reversed(word)) and len(word) > len(longest_palindrome):
        longest_palindrome = word
'''

for word in scrabble.wordlist :
    if word == word[::-1] and len(word) > len(longest_palindrome):
        longest_palindrome = word

print(longest_palindrome)