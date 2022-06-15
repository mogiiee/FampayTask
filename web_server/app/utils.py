#gives a dictionary rooted with regex expressions to be put into the advanced search 

def GetAdvancedSearchString(query):
    list_query = query.split(" ")
    base_dict = {"$or": []}
    for i in list_query:
        # defining title dict
        title_dict = {
            "title": {"$regex": i, "$options":"i"}
        }
        description_dict = {
            "description": {"$regex": i, "$options":"i"}
        }
        base_dict["$or"].append(title_dict)
        base_dict["$or"].append(description_dict)

    return base_dict