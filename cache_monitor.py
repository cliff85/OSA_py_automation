#!/usr/bin/env python
 
import re
import sys
import urllib
import urlparse
from BeautifulSoup import BeautifulSoup
 
class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
 
def process(url):
    print url
    myopener = MyOpener()
    page = myopener.open(url+"/statistics.jsp")
    disk_page = myopener.open(url+"/diskStatistics.jsp")
    text = page.read()
    disktext = disk_page.read()
    page.close()
    disk_page.close()
 
    soup = BeautifulSoup(text)
# <Cache Hits>/(<Cache Hits>+<Cache Misses>)
# Hits - 5 Misses - 6
    _list=[]
    table = soup.find('table', id="statistics")
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
	    _list.append(td.string.strip())
    print _list[4], _list[5]
    print _list[6], _list[7]
    print float(_list[5])/(float(_list[5])+float(_list[7]))
    soup = BeautifulSoup(disktext)
    _disklist=[]
    table = soup.find('table', cellspacing='1')
    rows = table.findAll('tr')
    for tr in rows:
        cols = tr.findAll('td')
        for td in cols:
            _disklist.append(td.string.strip())
    print _disklist[2], _disklist[3], "\n"
def main():
    if len(sys.argv) == 1:
        sys.exit(-1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
	url = url.rstrip('\\')
        process(url)
 
if __name__ == "__main__":
    main()
