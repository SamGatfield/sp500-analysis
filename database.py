import sqlite3


# Creating db with passed in name and table name from data in passed in data frame

def save_to_db(dataframe, db_name, table_name):
    conn = sqlite3.connect(db_name)
    dataframe.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()


def check_rsi_range(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = f"SELECT MIN(RSI), MAX(RSI) FROM {table_name}"
    result = cursor.execute(query).fetchone()
    conn.close()
    return result

# Checking RSI values to see when SP500 was overbought, oversold or normal

def rsi_signals(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    query = f"""
    SELECT date(Date), RSI
    FROM {table_name}
    """
    results = cursor.execute(query).fetchall()
    conn.close()

    signals = []
    for date, rsi in results:
        if rsi is None:
            continue
        rsi = round(rsi, 2)
        if rsi < 30:
            signal = "oversold"
        elif rsi > 70:
            signal = "overbought"
        else:
            signal = "normal"
        signals.append((date, rsi, signal))
    return signals

