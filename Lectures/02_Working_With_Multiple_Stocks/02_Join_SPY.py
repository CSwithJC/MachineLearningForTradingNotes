""" Join the SPY Data into our Dataframe"""

import pandas as pd


def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'

    # this creates an array of dates in the range given:
    dates = pd.date_range(start_date, end_date)

    # create empty dataframe with dates above
    df1 = pd.DataFrame(index=dates)

    # Read SPY Data into temporary dataframe
    dfSPY = pd.read_csv("../../data/SPY.csv")

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY) # .join does left join by defaults
    print df1
    # This prints lots of NaNs because dfSPY uses the standard int primary key (not the dates)

if __name__ == "__main__":
    test_run()