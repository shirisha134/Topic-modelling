from mongo import load_from_mongo
from mongo import save_to_mongo




stopwords_file='stopwords.txt'
stop_lis=[]
def stopwords_list(filename):
    with open(filename,'r') as f:
        for line in f:
            line=line.replace('\n','')
            stop_lis.append(line)
stopwords_list(stopwords_file)


def remove_stopwords(text):
    text = ' '.join([word for word in text.split() if word not \
                     in stop_lis])
    return text


docs_before=load_from_mongo("hindu","docs1")
for each in docs_before:
    each["text"]=remove_stopwords(each["text"])
    save_to_mongo(each,"hindu_modified","docs1")
    
