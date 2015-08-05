__author__ = 'eugene'

import scraperwiki
from lxml import etree
import lxml.html
import string
from datetime import datetime
import csv
import urllib
import re

def getHousesCount(suburb, postCode):

    html = scraperwiki.scrape("http://www.realestate.com.au/buy/with-3-bedrooms-in-" + re.sub(" ","+",suburb) + "%2c+vic+" + postCode + "%3b/list-1?includeSurrounding=false")

    #root = etree.HTML(html)

    root = lxml.html.fromstring(html)

    el = root.cssselect("div.resultsInfo p")[0]

    #for el in root.cssselect("div.resultsInfo p"):

    #    if string.inde

    a = string.split(el.text," ")
    cnt = a[len(a)-3]

    # Save found data
    scraperwiki.sqlite.save(unique_keys=['extracted_on','suburb'], data={
        "extracted_on": extractedOn,
        "suburb": suburb,
	"3_bedroom_count": cnt
        })

    print suburb + " " + a[len(a)-3] 


extractedOn = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
dictReader = csv.DictReader(open('Suburbs.csv', 'rb'))

for line in dictReader:
    getHousesCount(line['Suburb'], line['PostCode'])

