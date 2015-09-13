from pymongo import MongoClient
import re

con = MongoClient('localhost')
coll = con.hindu_modified.docs1

text = ''
for each in coll.find():
	text=text+each['text']

text = re.sub(r'[^a-zA-Z0-9 ]',' ',text)

text_tokens=text.split(' ')
text_dist={}
for each in text_tokens:
	if each.lower() in text_dist.keys():
		text_dist[each.lower()] =text_dist[each.lower()]+1
	else:
		text_dist[each.lower()] = 1
		


f= open('vocab.txt','w')

        
for each in text_dist.keys():
	f.write(each)
	f.write('\n')
	
