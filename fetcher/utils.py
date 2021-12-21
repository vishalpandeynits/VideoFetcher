import requests
from random import choice
from videofetcher.keys import API_KEYS as KEYS
from .models import Video

YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
PUBLISHED_AFTER = '2020-01-01T00:00:00.000Z'
QUERY_STRINGS = ['india', 'america', 'britain', 'football', 'cricket', 'official', 'what', 'how', 'russia', 'new']

def search_videos(max_results = 60, order = 'date'):
    """
    Youtube search function

    params: 
        query:query for which we want to fetch videos
        part:snippet, contentDetails, player, statistics, status. default: snippet
        max_result: limits number of items in query
        order: basis of sort
    return:
        returns a json response from youtube data api v3.
    """
    if not KEYS:
        print("APIS KEYS NOT FOUND, add API keys into API_KEYS list of /fetcher/keys.py file.")
        return None

    params = {
        'q':choice(QUERY_STRINGS), 
        'maxResults': max_results,
        'publishedAfter':PUBLISHED_AFTER, 
        'order': order, 
        'type': 'video',
        'part': "snippet", 
    }

    error_json = [] # records error
    for key in KEYS:
        params.update(**{'key':key}) # add keys into params
        res = requests.get(YOUTUBE_SEARCH_URL, params = params)
        if res.status_code == 200:
            data = res.json()
            return data
        else:
            error_json.append(res.json())

    if error_json:
        print(error_json) # list out all errors
        
    return None

def format_data(data):
    """
        Accepts the response returned by Youtube API and returns
        a formatted list of dictionary containing required keys
    """
    video_list = []
    if data is None:
        return video_list
        
    items = data.get('items')
    for item in items:
        video = {
            'video_id':item['id']['videoId'],
            'title': item['snippet']['title'], 
            'description': item['snippet']['description'],
            'published_on': item['snippet']['publishTime'],
            'channel':item['snippet']['channelTitle'],
            'thumbnail_url': item['snippet']['thumbnails']['default']['url'],
        }
        video_list.append(video)
    return video_list

def update_new_videos():
    """
    Accepts data from search function, formats the required data,
    and bulk create into database.
    """
    data = search_videos()
    videos = format_data(data)
    
    # create a list of Video instances
    video_instances = [
        Video(**video) for video in videos
    ]
    # Bulk create records, skip if received any duplicate video(same video id).
    created = Video.objects.bulk_create(video_instances, ignore_conflicts = True)
    if created:
        print("New list of videos updated into database.")
    return bool(created)