from . import database, responses, utils, api

#Inserts the data recieved from the Google api 
def Inserter(number_of_inserts, insert_query):
    list_of_entries = api.YoutubeCaller(number_of_inserts, insert_query)
    if len(list_of_entries) == 0:
        pass
    else:
        database.collection.insert_many(list_of_entries)
    return responses.ResponseStruct(True, None, {
        "inserted_count": int(len(list_of_entries)),
        # "inserted_data": list_of_entries
    })

#OG search which can take multiple words in any format and search the description and the title

def Search(query, limit, page):    
    page = int(page)
    limit = int(limit)
    if int(page) == 0:
        return responses.ResponseStruct(False, "page cannot be less than 1", None)
    skip = (page - 1) * limit

    search_term = utils.GetAdvancedSearchString(query)
    # search
    searched = database.collection.find(search_term, {"title": 1,"description":1, "_id": 0}).limit(limit).skip(skip).sort("_id", -1)
    results = list(searched)

    # results
    if len(results) == 0:
        return responses.ResponseStruct(False, "zero results", None)
    else:
        return responses.ResponseStruct(True, "results found", results)

#Gets the data in a paginated format

def GetData(limit, page):
    page = int(page)
    limit = int(limit)

    if int(page) == 0:
        return responses.ResponseStruct(False, "page cannot be less than 1", None)
    skip = (page - 1) * limit #logic for the page,limit and skip function
    try:
        results = database.collection.find({}, {"_id": 0}).limit(limit).skip(skip).sort("_id", -1)
        return responses.ResponseStruct(True, "results fetched", list(results))
    except Exception as e:
        return responses.ResponseStruct(False, str(e), None)
