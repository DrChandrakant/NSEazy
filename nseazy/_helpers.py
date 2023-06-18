import requests
import time

_headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'DNT': '1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    
}

def get_cookies(_base_api_url):
    session = requests.Session()
    request = session.get(_base_api_url,headers=_headers)
    if request.status_code == 200:
        cookies = dict(request.cookies)
    else:
        time.sleep(5)
        request = session.get(_base_api_url,headers=_headers)
        cookies = dict(request.cookies)
    return cookies


_base_api_url = "https://www.nseindia.com/"

_equity_quote_api = "api/quote-equity?symbol="

_derivative_quote_api = 'api/quote-derivative?symbol='

_option_chain_api = 'api/option-chain-indices?symbol='

_holidays_api = 'api/holiday-master?type='

_cookies = get_cookies(_base_api_url)


