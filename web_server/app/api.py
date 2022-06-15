from . import time_manager, exporter
from datetime import datetime
from googleapiclient.discovery import build

def YoutubeCaller(number, insert_query):
    try:
        service = build('youtube', 'v3', developerKey= exporter.API_KEY_1) 
        #put in your own api key from the .env file
    except:
        service = build('youtube', 'v3', developerKey= exporter.API_KEY_2) 
        print("used api key 2")
        #put in your own api key2 from the .env file
        #api_key2 will only kick in when api_key 1 fails
    timern = time_manager.get_yt_datetime()
    query = str(insert_query)
    req = service.search().list(part = 'snippet', q = query, maxResults= number, type='video', order= 'date', publishedAfter= timern)
    response = req.execute()
    items = response["items"]
    mongo_list = []
    #looping through the dict to find the required values
    for i in items:
        mongo_input = {}
        mongo_input["video_id"] = i["id"]["videoId"]
        mongo_input["channel_title"] = i["snippet"]["channelTitle"]
        mongo_input["description"] = i["snippet"]["description"]
        mongo_input["title"] = i["snippet"]["title"]
        mongo_input['publishing_datetime'] = i["snippet"]["publishTime"] 
        mongo_input["timestamp"] = datetime.now()
        mongo_input['thubnail_url1']  = i["snippet"]["thumbnails"]["default"]["url"]
        mongo_input['thubnail_url2']  = i["snippet"]["thumbnails"]["high"]["url"]
        mongo_input['thubnail_url3']  = i["snippet"]["thumbnails"]["medium"]["url"]

        mongo_list.append(mongo_input)
    
    return mongo_list
