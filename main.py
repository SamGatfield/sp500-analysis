import pandas as pd 
import mplfinance as mpf

from load_data import read_csv

from plotting import candle_plot

from database import save_to_db, rsi_signals, check_rsi_range

from indicators import sma_indicator,rsi_indicator, macd_indicator


df = read_csv("data/sp 500.csv")


# Check for duplicates

no_of_rows = len(df.index)

#print(no_of_rows)

for i in range (0, no_of_rows):
    if df.duplicated()[i] == True:
        df.drop_duplicates(inplace = True)
    else:
        continue
    
#print(df.head())


# PLOTTING

mc = mpf.make_marketcolors(up="lime", down="r", inherit=True)
my_style = mpf.make_mpf_style(base_mpf_style="nightclouds", marketcolors=mc)

candle_plot(df, 2000,2005, my_style)


# INDICATORS

sma_indicator(df, 20, 50)
rsi_indicator(df, 14)
macd_indicator(df)


#print(df.tail())

# DATABASE

save_to_db(df,"data/sp500_data.db", "sp500_table")

rsi_range = check_rsi_range("data/sp500_data.db", "sp500_table")

signals = rsi_signals("data/sp500_data.db", "sp500_table")


overbought_days = 0
oversold_days = 0
normal_days = 0

for date, rsi, label in signals:
    if label == "overbought":
        overbought_days += 1
    elif label == "oversold":
        oversold_days += 1
    else:
        normal_days += 1

print(f"The total overbought days were: {overbought_days}"
      f"\nThe total oversold days were: {oversold_days}"
      f"\nThe total normal days were: {normal_days}"
      )

check = input("If you would like to see all dates where SP500 was overbought, oversold and normal, type y: ")
if check.lower() == "y":
    for date, rsi, label in signals:
        print(f"On {date}, the SP500 was {label} (RSI = {rsi})")
else:
    pass
