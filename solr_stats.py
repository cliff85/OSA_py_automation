#!/usr/bin/env python
 
import re
import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
 
class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'
 
def process(url):
    print url
    myopener = MyOpener()
    page = myopener.open(url)
    text = page.read()
    page.close()
 
    soup = BeautifulSoup(text)
    cache = soup.cache.find_all('name')
    _name_list=[]
    for i in cache:
        _name_list.append(i.contents[0].strip())
    _hitratio = []
    hitratio = soup.cache.find_all('stat', attrs = {'name':'hitratio'})
    for i in hitratio:
        _hitratio.append(i.contents[0].strip())
    cumulative_hitratio = soup.cache.find_all('stat', attrs = {'name':'cumulative_hitratio'})
    _cumulative_hitratio = []
    for i in cumulative_hitratio:
        _cumulative_hitratio.append(i.contents[0].strip())
    for n, h, c in zip(_name_list, _hitratio, _cumulative_hitratio):
        print "Cache :", n
        print "Hit Ratio :", h
        print "Cumulative Hitratio :", c

def main():
    if len(sys.argv) == 1:
        sys.exit(-1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
	url = url.rstrip('\\')
        process(url)
 
if __name__ == "__main__":
    main()


#####Dev
#soup.cache # contains cache info
#cache = soup.cache.find_all('name') #gives all names
#hitratio = soup.find_all('stat', attrs = {'name':'hitratio'}) #Makes a list of all statistics
#cumulative_hitratio = soup.find_all('stat', attrs = {'name':'cumulative_hitratio'}) #Makes list of all cumulative hit ratio

#Get just the #'s'
#for i in hitratio:
#    print i.contents[0].strip()