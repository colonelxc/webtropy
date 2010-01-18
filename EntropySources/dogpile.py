#
#  dogpile.py
#  webtropy
#
#  Created by Ben Sanders on 10/11/09.
#  Copyright (c) 2009
#

import subprocess
import re
from BeautifulSoup import BeautifulStoneSoup

# Time in seconds
min_time_between_requests=10

def getTerms():
    """Returns a strings that a human might search for
    
    Get search terms from dogpile search spy
    """
    try:
        proc = subprocess.Popen("cat dogpile.txt | nc www.dogpile.com 80",cwd="./EntropySources/",shell=True,stdout=subprocess.PIPE)
        out = proc.communicate()[0]
    except OSError, e:
        return None
        
    reg = re.compile('[\w\W]+\r\n\r\n')
    xml = BeautifulStoneSoup(out[reg.match(out).end():])
    
    taglist = xml.findAll('title', recursive=True)
    strlist = []
    for tag in taglist:
        strlist.append(tag.string)
        
    #print out
    return strlist
    
    