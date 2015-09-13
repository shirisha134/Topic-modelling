from mongo import load_from_mongo
import numpy as np
import re
import lda
feature_array=[]
result=load_from_mongo("hindu_modified","docs1")
f=open('vocab.txt','r')
feature_vector=f.read().split('\n')
#print len(feature_vector)
len_of_feature_vector=len(feature_vector)
#print feature_vector[:10]

for each in result:
   
    text=each["text"]
    #print text
    text = re.sub(r'[^a-zA-Z0-9 ]',' ',text)
    text_tokens=text.split(" ")
    
    text_dist={}
    for each in text_tokens:
        if each.lower() in text_dist.keys():
            text_dist[each.lower()] =text_dist[each.lower()]+1
        else:
            text_dist[each.lower()] = 1
    vector=[0]*len_of_feature_vector
    for each in text_dist.keys():
      
        #print feature_vector.index(each)
        
        vector[feature_vector.index(each)]=text_dist[each]
    feature_array.append(vector)
    

print len(feature_array)
model=lda.LDA(n_topics=10,n_iter=500,random_state=1)
model.fit(feature_array)
topic_word=model.topic_word_
n_top_words=7
for i,topic_dist in enumerate(topic_word):
    topic_words=np.array(tuple(feature_vector))[np.argsort(topic_dist)][:-n_top_words:-1]
    print ("topic {}:{}".format(i, " ".join(topic_words)))


##titles=[each['HD'] for each in result]
##titles=tuple(titles)
##
##for i in range(5):
##	print("{} (index-{}))".format(titles[i],i))
