import requests
from random import choice
from decouple import config

YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
PUBLISHED_AFTER = '2020-01-01T00:00:00.000Z'
KEYS = config('KEYS').split('|')
QUERY_STRINGS = ['india', 'america', 'britain', 'football', 'cricket', 'official', 'what', 'how', 'russia', 'new']

def search_videos(query = 'india', part = 'snippet', max_results = 20, order = 'date'):
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
    params = {
        'q':choice(QUERY_STRINGS), 
        'maxResults': max_results,
        'publishedAfter':PUBLISHED_AFTER, 
        'order': order, 
        'type': 'video',
        'part': "snippet", 
    }
    error_json = []
    for key in KEYS:
        params.update(**{'key':key,})
        res = requests.get(YOUTUBE_SEARCH_URL, params = params)
        if res.status_code == 200:
            data = res.json()
            return data
        else:
            error_json.append(res.json())

    if error_json:
        print(error_json)
        
    return None

def format_data(data):
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