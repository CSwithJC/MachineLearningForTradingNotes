""" More Slicing """

import os
import pandas as pd


def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join("../../../" + base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY': # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'IBM', 'GLD']

    # Get stock data
    df = get_data(symbols, dates)

    # MORE SLICING:
    # Slice by row range (dates) using DataFrame.ix[] selector
    print 'Slice By Row:'
    print df.ix['2010-01-01':'2010-01-31'] # The Month of January

    # Slice by Column (Symbols)
    print 'Slice by Column (GOOG)'
    print df['GOOG'] # a single label selects a single column

    print 'Slice by Column (IBM and GLD)'
    print df[['IBM', 'GLD']] # a list of labels selects multiple columns

    # Slice through both dimensions (rows and columns)
    print 'Slice by row and column:'
    print df.ix['2010-03-10':'2010-03-15', ['SPY', 'IBM']]

if __name__ == "__main__":
    test_run()
