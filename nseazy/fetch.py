import pandas as pd
from nseazy._helpers import _base_api_url, _equity_quote_api, _derivative_quote_api
from nseazy._instruments import _validate_symbol , fnolist
from nseazy._generate_request import _fetch_data



def nse_quote(symbol,section=""):
    symbol = _validate_symbol(symbol)

    if(section==""):
        if any(x in symbol for x in fnolist):
            api_url = _fetch_data( _base_api_url + _derivative_quote_api + symbol)
        else:
            api_url = _fetch_data( _base_api_url + _equity_quote_api + symbol)
        return api_url

    if(section!=""):
        api_url = _fetch_data( _base_api_url + _equity_quote_api + symbol+'&section='+section)
        return api_url