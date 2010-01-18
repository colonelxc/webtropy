#
#  EntropyQueue.py
#  webtropy
#
#  Created by Ben Sanders on 10/11/09.
#  Copyright (c) 2009
#

import threading, Queue, random, time, calendar
from EntropySources import dogpile
from EntropySources import googlehottrends
from EntropySources import wordlist

# URL entropy queue
urls = Queue.Queue(1000)

class EntropyQueue(threading.Thread):
    """worker thread that generates urls to visit for the url queue"""
    
    rand = random.Random()
    
    sourcelist = []
    
    
    def run(self):
        """loops and pulls data from various sources, when needed"""
        self.rand.seed()
        timestamp = calendar.timegm(time.gmtime())
        
        # Add sources here (and in the import statements)
        # tuple is of the form:
        # ("next_time_we_can_run_this_function,source.min_time_between_requests,source.getTerms())
        #self.sourcelist.append((0,dogpile.min_time_between_requests,dogpile.getTerms))
        #self.sourcelist.append((0,googlehottrends.min_time_between_requests,googlehottrends.getTerms))
        self.sourcelist.append((0,wordlist.min_time_between_requests,wordlist.getTerms))
        
        while True:
            if not urls.full():
                terms = self.generateTerms()
                searchurls = self.generateUrlsFromTerms(termlist=terms)
                for searchurl in searchurls:
                    urls.put(searchurl)
                    
                print urls.qsize()
                time.sleep(10)
            else:
                print "full"
                time.sleep(10)


    def generateTerms(self):
        """returns a list of search terms"""
        
        #pick a search generation method
        self.sourcelist.sort()
        
        source = self.sourcelist.pop(0)
        print "first=" + str(source[0]) + " second=" + str(source[1])
        termlist = source[2]()
        
        self.sourcelist.append((calendar.timegm(time.gmtime()) + source[1],source[1],source[2]))
        
        return termlist
        
    def generateUrlsFromTerms(self, termlist=[]):
        """creates search queries for various terms"""
        
        urllist = []
        
        if termlist == None:
            return []
        
        for term in termlist:
            searchengine = self.rand.randint(1,3)
            if searchengine == 1:
                urllist.append("http://www.google.com/q=" + term)
            elif searchengine == 2:
                urllist.append("http://search.yahoo.com/search?p=" + term)
            elif searchengine == 3:
                urllist.append("http://www.bing.com/search?q=" + term)
                
        return urllist