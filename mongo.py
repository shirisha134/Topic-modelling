import json
import pymongo
import sys

#Saving to MongoDB

def save_to_mongo(data,mongo_db,mongo_db_coll,**mongo_conn_kw):
    client = pymongo.MongoClient('localhost',27017)
    db=client[mongo_db]
    coll=db[mongo_db_coll]
    try:
        return coll.insert(data)
    except:
        print "Unexpected error:", sys.exc_info()[0]


#Loading from MongoDB      
def load_from_mongo(mongo_db,mongo_db_coll,
                    return_cursor=False,criteria=None,projection=None,
                    **mongo_conn_kw):
    client = pymongo.MongoClient('localhost',27017)
    db=client[mongo_db]
    coll=db[mongo_db_coll]
    if criteria is None:
        criteria={}
    if projection is None:
        cursor = coll.find(criteria)
    else:
        cursor = coll.find(criteria,projection)
    if return_cursor:
        return cursor
    else:
        return [item for item in cursor]
