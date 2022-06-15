import pymongo
from . import exporter



#ALL the database information is given here. Add your credentials, db name, and collection name specified in the places below
client = pymongo.MongoClient(exporter.MONGO_DB_CRED)
db = client[exporter.DB_NAME]
collection = db[exporter.COLLECTION]


 
