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
        'Future'    : { 'Default'       : False,
                          'Description' : "If Derivative Segment Data Required. Set True ",
                          'Validator'   : lambda value: isinstance(value,bool) },
        'Info'      : { 'Default'       : False,
                          'Description' : "If Company Information Required. Set True ",
                          'Validator'   : lambda value: isinstance(value,bool) },
        'LTP'       : { 'Default'       : True,
                          'Description' : "If Last Traded Price(LTP) Required. Set True ",
                          'Validator'   : lambda value: isinstance(value,bool) },
        'OHLCV'     : { 'Default'       : False,
                          'Description' : "If Open High Low Close and Volumne Data Required. Set True ",
                          'Validator'   : lambda value: isinstance(value,bool) },
        'Pre'       : { 'Default'       : False,
                          'Description' : "If Pre Open Market Data Required. Set True ",
                          'Validator'   : lambda value: isinstance(value,bool) },     
    }
    _validate_vkwargs_dict(vkwargs)
    return vkwargs

def show_data(symbol,kwargs):

    symbol, isDerivative = _validate_symbol(symbol)

    config = _check_kwargs(kwargs, _get_quote_parameter())


    Future = config['Future']
    Info   = config['Info']
    OHLCV  = config['OHLCV']
    Popen  = config['Pre']



    if Future == True:
        data = quote_derivative(symbol)
        print(data)
    
    if Future == False:
        data = quote_equity(symbol)
        company_info = {
            'Name'          : data['info']['companyName'],
            'Symbol'        : data['info']['symbol'],
            'Sector'        : data['info']['industry'],
            'ISIN'          : data['metadata']['isin'],
            'Sector PE'     : data['metadata']['pdSectorPe'],
            'PE'            : data['metadata']['pdSymbolPe'],
            'Index'         : data['metadata']['pdSectorInd'],
            'Face Value'    : data['securityInfo']['faceValue'],
            'Total Equity'  : data['securityInfo']['issuedSize']
        }
        olhc = {
            'Open'         : data['priceInfo']['open'],
            'LTP'          : data['priceInfo']['lastPrice'],
            'Change'       : data['priceInfo']['change'],
            '% Chg'        : round(data['priceInfo']['pChange'],2),
            'Final Close'  : data['priceInfo']['close'],
            'Previous'     : data['priceInfo']['previousClose'],
            'VWAP'         : data['priceInfo']['vwap'],
            'Lower Circuit': data['priceInfo']['lowerCP'],
            'Upper Circuit': data['priceInfo']['upperCP'],
        }

        df_info = pd.DataFrame([company_info])
        df_olhc = pd.DataFrame([olhc])
        ltp =  data['priceInfo']['lastPrice']
    if Info == True:
        print(df_info)
    if OHLCV == True:
        print(df_olhc)
    if config['LTP'] == True:
        print(ltp)


