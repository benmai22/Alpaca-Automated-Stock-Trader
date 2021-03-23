from main import *

CLOCK = clock()
MARKET_OPEN = CLOCK['is_open']

tickers = ['AAPL', 'MSFT']

while MARKET_OPEN is True:
    for tick in tickers:
        order = create_order(tick, 1, 'buy', 'market', 'day')
else:
    print('Market is closed until: ' + str(CLOCK['next_open']))
