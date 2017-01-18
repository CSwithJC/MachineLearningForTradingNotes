''' Building a dataframe in pandas '''
import pandas as pd
import os

def symbol_to_path(symbol, base_dir="data"):
    ''' Return CSV File Path Given to Ticker Symbol '''
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def test_run():
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date, end_date)
    print dates

    # Create an empty dataframe
    df1 = pd.DataFrame(index=dates)

    # Read SPY data into temporary dataframe
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True,
                        usecols=['Date', 'Adj Close'],
                        na_values=['nan'])

    # Rename 'Adj Close' column to 'SPY' to prevent clash
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})

    # Join the two dataframes using DataFrame.join
    df1 = df1.join(dfSPY, how='inner')

    # Drop NaN Values
    #df1 = df1.dropna()

    # Read in more stocks
    symbols = ['GOOG', 'IBM', 'GLD']
    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='Date',
                              parse_dates=True, usecols=['Date', 'Adj Close'],
                              na_values=['nan'])

        #rename to prevent clash
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df1 = df1.join(df_temp) #use default how='left'

    print df1

if __name__ == "__main__":
    test_run()