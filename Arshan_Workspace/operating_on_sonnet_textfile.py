# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 19:24:05 2019

@author: sudachar
"""

import string

sonnet = open ('sonnets.txt', 'r').readlines()
sowpods = set([letter.strip() for letter in open('sowpods.txt', 'r')])
sonnet_words = set()

def remove_punctuation(word) :
    word.replace('-', ' ')
    apostrophe_idx = word.find("'")
    
    if apostrophe_idx != -1 :
        return None
    return word.strip(string.punctuation)

for line in sonnet :
    line_words = line.replace('-', ' ').strip().split()
    
    if len(line_words) <= 1 :
        continue
    
    for word in line_words :
        stripped_word = remove_punctuation(word)
        
        if stripped_word and len(stripped_word) > 1:
            sonnet_words.add(stripped_word.upper())
            
sonnet_words = list(sonnet_words)
sonnet_words.sort()

file_to_write = open('sorted words from sonnets text file.txt', 'w')
for word in sonnet_words :
    file_to_write.write(word + '\n')
file_to_write.close()
            
    

