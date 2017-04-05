""" Scatterplots with Alpha and Beta """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from util import get_data, plot_data


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()  # copy given DataFrame to match size and column names
    daily_returns[1:] = (df[1:] / df[:-1].values) - 1
    daily_returns.ix[0, :] = 0  # set daily returns for row 0 to 0
    return daily_returns


def test_run():

    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols = ['SPY', 'XOM', 'GLD']
    df = get_data(symbols, dates)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)

    # Scatterplot SPY vs XOM
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    # uses lime equation y = mx + b
    print "beta_XOM= ", beta_XOM
    print "alpha_XOM= ", alpha_XOM
    plt.plot(daily_returns['SPY'], beta_XOM * daily_returns['SPY'] + alpha_XOM, '-', color='r')
    plt.show()

    # Scatterplot SPY vs GLD
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    # uses lime equation y = mx + b
    print "beta_GLD= ", beta_XOM
    print "alpha_GLD= ", alpha_XOM
    plt.plot(daily_returns['SPY'], beta_XOM * daily_returns['SPY'] + alpha_XOM, '-', color='r')

    # Calculate correlation coefficient
    print daily_returns.corr(method='pearson')

    plt.show()

if __name__ == "__main__":
    test_run()