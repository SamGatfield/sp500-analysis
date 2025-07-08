import pandas as pd

def read_csv(csv):
    df = pd.read_csv(csv)

    df.drop("Adj Close", axis=1, inplace=True)

    columns = list(df)

    for column in columns[:]:
    # Change the format of the date
        if column == "Date":
            df[column] = pd.to_datetime(df[column])

        # Change datatypes of remaining columns (except date)
        else:
            df[column] = df[column].str.replace(",","",regex=False).astype(float)
            
    return df 