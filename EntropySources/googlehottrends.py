#
#  googlehottrends.py
#  webtropy
#
#  Created by Ben Sanders on 10/19/09.
#  Copyright (c) 2009 
#

import subprocess
import re
import urllib2
from BeautifulSoup import BeautifulSoup

# Time in seconds
#min_time_between_requests=10800 # 3 hours
min_time_between_requests=124

def getTerms():
    """Returns a strings that a human might search for
    
    Get search terms from google hot trends
    """
    
    headers = { 'User-Agent' : 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5', \
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', \
    'Accept-Language' : 'en-us,en;q=0.5' }
    
    request = urllib2.Request( 'http://www.google.com/trends/hottrends', None, headers )
    
    try:
        httphandle = urllib2.urlopen(request)
    
    except URLError, e:
        return None
        
    html = BeautifulSoup(httphandle.read())
    
    tables = html.findAll('table', attrs={"class" : "Z2_list"}, recursive=True)
    trends = []
    for table in tables:
        trends.extend(table.findAll('a', recursive=True))
        
    strlist = []
    for i in range(len(trends)):
        if i >= 3:
            strlist.append(trends[i].string)
    
    return strlist