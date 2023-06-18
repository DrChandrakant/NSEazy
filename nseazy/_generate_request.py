from nseazy._helpers import _headers, _cookies
import requests


method = True

if(method is True):
    def _fetch_data(api_url):
        session = requests.Session()
        rawData = session.get(api_url,headers=_headers,cookies=_cookies).json()
        return rawData