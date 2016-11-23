import requests

class AzureApiClient(object):
    """Azure Remote Api Http Client"""
    def __init__(self, url):
        self.url = url

    def post(self, json):
        """Post json data to the external azureML configured endpoint"""
        res = requests.post(self.url, json=json)
        return res