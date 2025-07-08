import mplfinance as mpf

from indicators import sma_indicator, rsi_indicator, macd_indicator

def candle_plot(dataframe, start_year, end_year, s):

    dataframe = dataframe.iloc[::-1].reset_index(drop=True)
    dataframe = dataframe.set_index("Date")

    df_filtered = dataframe.loc[f"{start_year}-01-01":f"{end_year}-12-31"]

    mpf.plot(
        df_filtered,
        type = "candle",
        volume = True,
        figratio = (15,7), 
        style = s, 
        xlabel = "Date",
        ylabel = "Price (GBP)",
        title = f"\nS&P 500 prices between {start_year} and {end_year}",
        savefig = f"images/ohlc_chart_{start_year}_{end_year}.png"
    )

    mpf.show()