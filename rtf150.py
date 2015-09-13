from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.xhtml.writer import XHTMLWriter
from bs4 import BeautifulSoup
import sys,re
from pymongo import MongoClient

con = MongoClient('localhost')
coll = con.hindu.docs1

#filename="t_list.txt"
#f=open(filename,'w')
def perform(t=list()):
    temp = "".join([ch for ch in str(t[1]) if ord(ch)<=128 and ord(ch)!=63])
    initial = re.findall(">([a-zA-Z.,///? 0-9-]+)  <br/>",temp)
    #print initial
    if len(initial)<8:
        #print "Problem with initial length : %s " % (len(initial))
        return None
    #print initial
    g={}
    g['SE']= initial[0]
    g['HD']= re.findall(""">HD([.:a-zA-Z///? 0-9'",]+)  </strong>""",str(t[1]))[0] if len(re.findall(""">HD([.:a-zA-Z///? 0-9'",]+)  </strong>""",str(t[1]))) else "1234"
    g['BY'] = initial[1]
    g['WC'] = initial[2]
    g['PD'] = initial[3]
    g['SN'] = initial[4]
    g['SC'] = initial[5]
    g['PG'] = initial[6]
    g['LA'] = initial[7]

    g['text']=''
    for each in t[2:-1]:
        if each.find('strong'):
            if each.find('strong').text=='LP' or each.find('strong').text=='TD':
                g['text']=g['text']+each.text[2:]
            else:
                g['text']=g['text']+each.text
        else:
                g['text']+=" "+each.text

    #print g

    try:
        coll.insert(g)
    except Exception as e:
        print e
    print "+"*50


temp_file = open('Hindu 2007 201-200','r')
r = temp_file.read()
print "Read from HTML files Done"
soup = BeautifulSoup(r)
t=soup.find_all('p')

sub=[]

for every in t[1:]:
    sub.append(every)
    if every.find('strong'):
            if every.find('strong').text=='NS' or every.find('strong').text=='IN':
                i = perform(sub)
                sub=[]

