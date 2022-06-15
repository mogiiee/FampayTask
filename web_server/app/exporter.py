from dotenv import load_dotenv
import os
# load env variables at one place 
load_dotenv()

API_KEY_1 = os.environ.get('API_KEY_1')
API_KEY_2 = os.environ.get('API_KEY_2')

MONGO_DB_CRED = os.environ.get("MONGO_DB_CRED")
DB_NAME = os.environ.get("DB_NAME")
COLLECTION = os.environ.get('COLLECTION_NAME')

