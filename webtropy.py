#!/usr/bin/env python
#
#  webtropy.py
#  webtropy
#
#  Created by Ben Sanders on 10/11/09.
#  Copyright (c) 2009
#

import EntropyQueue, threading, time

entropy_queue = EntropyQueue.EntropyQueue()
entropy_queue.start()

class temp(threading.Thread):

    def run(self):
        while True:
            var= EntropyQueue.urls.get()
            print var
            time.sleep(5)


mythreads = []
for i in range(10):
    t = temp()
    mythreads.append(t)
    t.start()
    
    
