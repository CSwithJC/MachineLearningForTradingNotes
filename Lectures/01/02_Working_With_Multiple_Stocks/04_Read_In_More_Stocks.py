""" Add More Stocks to our DataFrame """

import pandas as pd


def test_run():

    start_date = '2010-01-22'
    end_date = '2010-01-26'

    # this creates an array of dates in the range given:
    dates = pd.date_range(start_date, end_date)

    # create empty dataframe with dates above
    df1 = pd.DataFrame(index=dates)

    # Read SPY Data into temporary dataframe

    # NOTE: index_col sets which value should be PK; parse_dates converts dates to Date Time Index Objects
    # NOTE: usecols selects only the columns that are wanted
    dfSPY = pd.read_csv("../../../data/SPY.csv", index_col="Date",
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    # Join the two dataframes using DataFrame.join()
    df1 = df1.join(dfSPY, how='inner') # .join does left join by defaults

    # Read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']

    # For loop that adds the rest of the new stocks and adds them to df1
    for symbol in symbols:
        df_temp = pd.read_csv("../../../data/{}.csv".format(symbol), index_col='Date',
                        parse_dates=True, usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

        #df = df1.join(df_temp) # uses default how='left'

        # the code above alone causes an error because column names are not unique; so add:

        # rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})

        df1=df1.join(df_temp) # uses default how='left'

    print df1

if __name__ == "__main__":
    test_run()