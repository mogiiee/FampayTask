# all the responses go from here in the format of status, message, data

def ResponseStruct(status, message, data):
    return {
        "status": status,
        "message": message,
        "data": data
    }
