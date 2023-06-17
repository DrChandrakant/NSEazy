import pandas as pd
from nseazy._helpers import _base_api_url, _equity_quote_api, _derivative_quote_api, _option_chain_api
from nseazy._instruments import _validate_symbol
from nseazy._generate_request import _fetch_data


def nse_quote(symbol,section=""):
    symbol, isDerivative = _validate_symbol(symbol)

    if(section==""):
        if isDerivative is True:
            rawJson = _fetch_data( _base_api_url + _derivative_quote_api + symbol)
        else:
            rawJson = _fetch_data( _base_api_url + _equity_quote_api + symbol)
        return rawJson

    if(section!=""):
        rawJson = _fetch_data( _base_api_url + _equity_quote_api + symbol+'&section='+section)
        return rawJson
    
def option_chain(symbol):
    symbol, isDerivative = _validate_symbol(symbol)
    if isDerivative is True:
        rawJson = _fetch_data( _base_api_url + _option_chain_api + symbol)
    else:
        rawJson = None
        raise ValueError(symbol, 'Not Listed In Derivative Segment Please Provide Symbol')
    return rawJson