from . import api
from . import database, responses, exporter

#inserting values in database
def Inserter():
    list_of_entries = api.YoutubeCaller(exporter.INSERT_VOLUME, exporter.INSERT_QUERY)
    if len(list_of_entries) == 0:
        pass
    else:
        database.collection.insert_many(list_of_entries)
    return responses.ResponseStruct(True, None, {
        "inserted_count": int(len(list_of_entries)),
    })



