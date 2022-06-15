from dotenv import load_dotenv
import os
# load env variables
load_dotenv()

#google api creds (youtube)
API_KEY_1 = os.environ.get('API_KEY_1')
API_KEY_2 = os.environ.get('API_KEY_2')

#database creds
MONGO_DB_CRED = os.environ.get("MONGO_DB_CRED")
DB_NAME = os.environ.get("DB_NAME")
COLLECTION = os.environ.get('COLLECTION_NAME')

#redis instantiation
REDIS_DB_CRED = os.environ.get('REDIS_DB_CRED')

#queries 
INSERT_QUERY = os.environ.get('INSERT_QUERY')
INSERT_VOLUME = int(os.environ.get('INSERT_VOLUME'))
