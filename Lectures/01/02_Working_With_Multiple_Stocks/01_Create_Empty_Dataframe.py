""" Build a dataframe in pandas """

import pandas as pd


def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'

    # this creates an array of dates in the range given:
    dates = pd.date_range(start_date, end_date)
    print dates

    # print the array elements like any array
    print dates[0]

    # create empty dataframe with dates above
    df1 = pd.DataFrame(index=dates) # the index= states that the dates will be the "primary key" of the dataframe
    print df1

if __name__ == "__main__":
    test_run()