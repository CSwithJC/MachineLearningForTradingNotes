""" Import CSV File """

import pandas as pd

def test_run():
    df = pd.read_csv("../../data/AAPL.csv")
    print df # Print Entire DataFrame
    print df.head() # Print First 5 Rows
    print df.tail() # Print Last 5 Rows

if __name__ == "__main__":
    test_run()