#!/usr/bin/env python

import sys
import urllib
import urlparse
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

def process(url):
    myopener = MyOpener()
    page = myopener.open(url)
    text = page.read()
    page.close()

    soup = BeautifulSoup(text)
    links = soup.find_all('a', attrs = {'class':'ibm-feature-link'})
    dates = soup.find_all('td', attrs = {'class':'ibm-numeric'})
    _newlist = []

    for l, d in zip (links, dates):
        if 'Security' in l.contents[0]:
            _tempdate = datetime.strptime(d.contents[0], '%d %b %Y')
            if (_tempdate + timedelta(days=30)) > datetime.now():
                _newlist.append([l.contents[0], l['href'], d.contents[0]])
    for v in _newlist:
        print "%s : %s" % (v[0], v[1])


def main():
    if len(sys.argv) == 1:
        sys.exit(-1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
        process(url)
# main()

if __name__ == "__main__":
    main()

#Using for Week 3 first check
#Make workable dates 
#testconv = datetime.s.trptime(dates[1].contents[0], '%d %b %Y')
