""" Using fillna """

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


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
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def compute_cumulative_returns(df):
    """Compute and return the daily return values."""

    cumulative_returns = df.copy()  # copy given DataFrame to match size and column names
    # Compute cumulative returns for row 1 onwards
    cumulative_returns[1:] = (df.ix[1:] / df.ix[0]) - 1
    cumulative_returns.ix[0, :] = 0  # set daily returns for row 0 to 0

    return cumulative_returns


def test_run():
    symbollist = ["FAKE2"]
    start_date = '2005-12-31'
    end_date = '2014-12-07'

    idx = pd.date_range(start_date, end_date)
    df_data = get_data(symbollist, idx)
    plot_data(df_data)

    # fill the gaps found in this dataset:
    df_data.fillna(method="ffill", inplace="TRUE")  # ffill fills forward, and inplace saves changes in same dataframe
    plot_data(df_data)

if __name__ == "__main__":
    test_run()
