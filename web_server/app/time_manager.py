from datetime import datetime, timedelta
#gives the current time for the getting information from youtube API
def get_yt_datetime():
    d = datetime.now() - timedelta(0, 1080)
    timern = d.isoformat('T')+"Z"
    return timern


