# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:40:59 2019

@author: sudachar
"""

import time

sonnet = [letter.strip() for letter in open('sonnet_words.txt', 'r').readlines()]
sowpod = [letter.strip() for letter in open('sowpods.txt', 'r').readlines()]
#word_dictionary = dict((letter, 1) for letter in sowpod) # the Dictionary way
word_set = set(sowpod)

counter = 0

start_timelog = time.time()

for word in sonnet :
    #if word not in word_dictionary :  # the Dictionary way
    if word not in word_set :
        print(word)
        
        counter += 1

stop_timelog = time.time()

print('Total new words : %d' %counter)
print('Total time elapsed : %1f seconds' %(stop_timelog - start_timelog))