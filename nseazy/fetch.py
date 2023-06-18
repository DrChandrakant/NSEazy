import pandas as pd
from nseazy._helpers import _base_api_url, _equity_quote_api, _derivative_quote_api, _holidays_api
from nseazy._instruments import _validate_symbol
from nseazy._generate_request import _fetch_data
from nseazy._validators import _validate_vkwargs_dict, _check_kwargs

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
    
def nse_optionchain_scrapper(symbol):
    symbol, isDerivative = _validate_symbol(symbol)
    if isDerivative is True:
        rawOptionchain = _fetch_data( _base_api_url + _derivative_quote_api + symbol)
    else:
        rawOptionchain = None
    return rawOptionchain

def nse_fno(symbol):
    symbol, isDerivative = _validate_symbol(symbol)
    try:
        rawJson = _fetch_data( _base_api_url + _derivative_quote_api + symbol)
        try:
            if(len(rawJson['stocks'])== 0):
                print(symbol,'May Not Be List In Derivative Segemnt. Trying Fetch Data From Equity Segment')
                rawJson = _fetch_data( _base_api_url + _equity_quote_api + symbol)
        except KeyError:
            pass
    except KeyError:
        print("Getting Error While Fetching.")
    return rawJson

def nse_eq(symbol):
    symbol, isDerivative = _validate_symbol(symbol)
    try:
        rawJson = _fetch_data( _base_api_url + _equity_quote_api + symbol)
        try:
            if(len(rawJson['stocks'])== 0):
                print(symbol,'May Not Be List In Equity Segemnt. Trying Fetch Data From Equity Segment')
                rawJson = _fetch_data( _base_api_url + _derivative_quote_api + symbol)
        except KeyError:
            pass
    except KeyError:
        print("Getting Error While Fetching.")
    return rawJson

def quote_equity(symbol):
    return nse_eq(symbol)

def quote_derivative(symbol):
    return nse_fno(symbol)

def option_chain(symbol):
    return nse_optionchain_scrapper(symbol)

def nse_holidays(type="trading"):
    if(type=="clearing"):
        rawHoliday = _fetch_data(_base_api_url+_holidays_api + type)
    if(type=="trading"):
        rawHoliday = _fetch_data(_base_api_url+_holidays_api + type)
    return rawHoliday



def _get_quote_parameter():
    vkwargs = {
        'Futures'     : { 'Default'     : False,
                          'Description' : "Is Listed In Derivative Segament. If Listed Set True ",
                          'Validator'   : lambda value: isinstance(value,bool) },
    }
    _validate_vkwargs_dict(vkwargs)
    return vkwargs

def show_data (symbol,**kwargs):
    config = _check_kwargs(kwargs, _get_quote_parameter())
    print(config)

    return dict( data=symbol, **config)