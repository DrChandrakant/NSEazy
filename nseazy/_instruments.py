from nseazy._generate_request import _fetch_data

def _validate_symbol(symbol):
    symbol = symbol.translate({ord('-'): None,ord('&'): None, }).upper()

    if any(x in symbol for x in fnolist):
        isDerivative = True
    else:
        isDerivative = False
    
    return symbol , isDerivative


def _instrument_derivative():
    positions = _fetch_data('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')

    nselist=['NIFTY','NIFTYIT','BANKNIFTY']

    i=0
    for x in range(i, len(positions['data'])):
        nselist=nselist+[positions['data'][x]['symbol']]

    return nselist

fnolist = _instrument_derivative()