from django.test import TestCase
import requests
from videofetcher.keys import API_KEYS as KEYS

YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

class FetcherTest(TestCase):
    def test_api_keys(self):
        """Tests if any of youtube api key provided is up and running. """

        assert len(KEYS), "APIS KEYS NOT FOUND, add it in KEYS list of /videofetcher/keys.py file."
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