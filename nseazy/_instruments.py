
from nseazy._generate_request import _fetch_data

def _validate_symbol(symbol):
    symbol = symbol.replace('&','%26')
    return symbol


def _validate_derivative():
    positions = _fetch_data('https://www.nseindia.com/api/equity-stockIndices?index=SECURITIES%20IN%20F%26O')

    nselist=['NIFTY','NIFTYIT','BANKNIFTY']

    i=0
    for x in range(i, len(positions['data'])):
        nselist=nselist+[positions['data'][x]['symbol']]

    return nselist

fnolist = _validate_derivative()