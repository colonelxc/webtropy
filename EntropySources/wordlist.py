#
#  wordlist.py
#  webtropy
#
#  Created by Ben Sanders on 11/25/09.
#  Copyright (c) 2009 
#

import os, sys, stat
import random

#Time in seconds
min_time_between_requests=100
wordlist_timestamp=0
wordlist = []
chunk_size = 50

def getTerms():
    wordlist_stat = os.stat('./EntropySources/wordlist.txt')
    if wordlist_stat.st_mtime > wordlist_timestamp:
        wordlist_timestamp = wordlist_stat.st_mtime
        read_file()
    elif wordlist.count() < chunk_size:
        read_file()
    
    returnlist = []
    for num in range(min(chunk_size,wordlist.count())):
        returnlist.append(wordlist.pop(0))
        
    return returnlist
    
        

def adjust_time(list_size=0):
    """Adjusts the min_time_between_requests so that if the wordlist doesn't change, we only reuse it once per hour."""
    if list_size == 0:
        return
    elif list_size < chunk_size:
        min_time_between_requests = 60*60
    else:
        temp = list_size / (chunk_size + 0.0)
        min_time_between_requests = int( 60*60 / list_size )
    

def read_file():
    temp_wordlist = []
    f = open('./EntropySources/wordlist.txt','r')
    for line in f:
        temp = str.strip(line)
        if temp != None:
            temp_wordlist.append(temp)
            
    random.shuffle(temp_wordlist)
    wordlist.extend(temp_wordlist)
    adjust_time(temp_wordlist.count())
    