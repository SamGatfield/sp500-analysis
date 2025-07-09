import streamlit as st 
import pandas as pd
import mplfinance as mpf

from load_data import read_csv
from indicators import sma_indicator, macd_indicator, rsi_indicator


df = read_csv("data/sp 500.csv")

sma_indicator(df, 20, 50)
rsi_indicator(df, 14)
macd_indicator(df)

st.title("S&P 500 Dashboard")



df["Date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df.set_index("Date", inplace=True)

min_year = df.index.year.min()
max_year = df.index.year.max()

# Lets the user decide the dates they want to look at

selected_years = st.slider(
    "Year range",
    min_value = int(min_year),
    max_value = int(max_year),
    value = (int(min_year), int(max_year))
)

start_year, end_year = selected_years
filtered_df = df[(df.index.year >= start_year) & (df.index.year <= end_year)]



st.subheader("Filtered data preview")
st.dataframe(filtered_df.tail(10))

st.subheader("Open and Close Prices")
st.line_chart(filtered_df[["Open", "Close"]].dropna())

st.subheader("Price")
st.line_chart(filtered_df[["Close", "SMA_20", "SMA_50"]].dropna())

st.subheader("RSI")
st.line_chart(filtered_df["RSI"].dropna())

st.subheader("MACD")
st.line_chart(filtered_df["MACD"].dropna())



