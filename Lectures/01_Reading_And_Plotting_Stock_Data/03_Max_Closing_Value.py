""" Compute Maximum Closing Price """

import pandas as pd

def get_max_close(symbol):
    """
    Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("../../../data/{}.csv".format(symbol))
    return df['Close'].max() # compute and return max

def test_run():
    for symbol in ['AAPL', 'IBM']:
        print "Max Close"
        print symbol, get_max_close(symbol)

if __name__ == "__main__":
    test_run()