import pandas as pd


def sma_indicator(dataframe, day_lower, day_upper):

    if day_lower >= day_upper:
        raise ValueError("Lower day must be smaller than the upper day")

    dataframe[f"SMA_{day_lower}"] = dataframe["Close"].rolling(window=day_lower).mean()
    dataframe[f"SMA_{day_upper}"] = dataframe["Close"].rolling(window=day_upper).mean()


def rsi_indicator(dataframe, days):
    delta = dataframe["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    gain_average = gain.rolling(days).mean()
    loss_average = loss.rolling(days).mean()

    realtive_strength = gain_average/loss_average
    dataframe["RSI"] = 100 - (100/(1+realtive_strength))


def macd_indicator(dataframe):
    exp_ma12 = dataframe["Close"].ewm(span=12, adjust=False).mean()
    exp_ma26 = dataframe["Close"].ewm(span=26, adjust=False).mean()

    dataframe["MACD"] = exp_ma12 - exp_ma26

    dataframe["Bullish"] = (dataframe["MACD"] > 0)
    dataframe["Bearish"] = (dataframe["MACD"] < 0)




