""" Compute Mean Volume """

import pandas as pd
import matplotlib.pyplot as plt

def get_max_close(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()


def get_mean_volume(symbol):
    """Return the mean volume for stock indicated by symbol.

    Note: Data for a stock is stored in file: data/<symbol>.csv
    """
    df = pd.read_csv("data/{}.csv".format(symbol))  # read in data
    return df['Volume'].mean()

def test_run():
    df = pd.read_csv("../../data/AAPL.csv")

    #plt.show()
    #print df #print entire dataframe
    #print df.head() #print
    #print df.tail()
    #print df[10:21] #rows between index 10 and 20

    #for symbol in ['AAPL', 'IBM']:
    #    print "Max Close"
    #    print symbol, get_max_close(symbol)
    #    print "Mean Volume"
    #    print symbol, get_mean_volume(symbol)

    print df['Adj Close']
    df['Adj Close'].plot()
    plt.show()

if __name__ == "__main__":
    test_run()