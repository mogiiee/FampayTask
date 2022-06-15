from fastapi import FastAPI
from . import ops, responses
#instantiating FastAPI

app = FastAPI()

#greetings and also the base EP
@app.get("/")
async def root():
    return responses.ResponseStruct(True, "Hello Fam", None)

# EP for inserting the info recieved from the API. One can also choose the number of entries and what to search too!!
@app.post("/insert")
async def insert(number_of_inserts, insert_query):
    try:
        response = ops.Inserter(number_of_inserts, insert_query)
        return response
    except Exception as e:
        return responses.ResponseStruct(False, str(e), None)


#EP for the OG search which can take multiple words in any format and search the description and the title
@app.get("/search")
async def Search(query, limit, page):
    try:
        results = ops.Search(query, limit, page)
        return results
    except Exception as e:
        return responses.ResponseStruct(False, str(e), None)

#gets all the data in a paginated format 
@app.get('/get_all_data')
async def get_all_data(limit, page):
    try:
        result = ops.GetData(limit, page)
        return result
    except Exception as e:
        return responses.ResponseStruct(False, str(e), None)
