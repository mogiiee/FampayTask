from datetime import datetime


#gives the current time for the getting information from youtube API
def get_yt_datetime():
    d = datetime.now()
    timern = d.isoformat('T')+"Z"
    return timern

