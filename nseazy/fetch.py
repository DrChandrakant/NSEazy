import os,sys
import requests
import pandas as pd
import json
import random
import datetime,time
import logging
import re
import urllib.parse
from nseazy._helpers import _headers, _base_api_url, _equity_quote_api, _derivative_quote_api, _cookies
from nseazy._instruments import _validate_symbol


method = True

if(method is True):
    def _fetch_data(api_url):
        rawData = requests.get(api_url,headers=_headers).json()
        return rawData

def nse_quote(symbol,section=""):
    symbol = _validate_symbol(symbol)

    if(section==""):
        if any(x in symbol for x in fnolist()):
            api_url = _fetch_data( _base_api_url + _derivative_quote_api + symbol)
        else:
            api_url = _fetch_data( _base_api_url + _equity_quote_api + symbol)
        return api_url

    if(section!=""):
        api_url = _fetch_data( _base_api_url + _equity_quote_api + symbol+'&section='+section)
        return api_url