from django.test import TestCase
from decouple import config
import requests
YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

class FetcherTest(TestCase):
    def test_api_keys(self):
        """Tests if any of youtube api provided in environment variable is up and running. """
        try:
            KEYS = config('KEYS').split('|')
        except Exception as ex:
            assert False, "APIS KEYS NOT FOUND, add it in your environment variables."
        running = False
        params = {
            'q':"india", 
            'maxResults': 10,
            'type': 'video',
            'part': "snippet", 
        }
        for key in KEYS:
            params.update(**{'key':key,})
            res = requests.get(YOUTUBE_SEARCH_URL, params = params)
            if res.status_code == 200:
                running = True
                break
        
        assert running, "None of your APIs are working"