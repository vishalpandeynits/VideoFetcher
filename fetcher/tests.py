from django.test import TestCase
import requests
from videofetcher.keys import API_KEYS as KEYS

YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

class FetcherTest(TestCase):

    def test_api_keys_available(self):
        """Tests if API keys are available."""

        self.assertNotEqual(KEYS, [] , "APIS KEYS NOT FOUND, add it in KEYS list of /videofetcher/keys.py file.")

    def test_api_key_validity(self):
        """ Test if API keys are valid, and our API is running."""
        params = {
            'q':"india", 
            'maxResults': 10,
            'type': 'video',
            'part': "snippet", 
        }

        running = False
        for key in KEYS:
            params.update(**{'key':key})
            res = requests.get(YOUTUBE_SEARCH_URL, params = params)
            if res.status_code == 200:
                running = True
                break

        self.assertFalse(not running, "None of your API Keys are running.")