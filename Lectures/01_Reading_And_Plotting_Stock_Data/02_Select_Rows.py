""" Select Rows From Dataframe """

import pandas as pd


def test_run():
    df = pd.read_csv("../../data/AAPL.csv")

    """ This is 'Slicing' """
    print df[10:21] # Rows Between Index 10 and 20


if __name__ == "__main__":
    test_run()