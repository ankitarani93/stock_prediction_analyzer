import yfinance as yf
import mysql.connector
import talib
from mysql.connector import Error
import pandas as pd
import time
from datetime import datetime

def static_table(v_symbol,v_shortname, v_sector,v_country):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO stock_details_static (symbol, shortName, sector, Country) VALUES (%s,%s,%s,%s)",(v_symbol,v_shortname,v_sector,v_country,))
    mydb.commit()

def variable_table(v_symbol,v_closePrice,v_Datetime):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO stock_details_variable (symbol, closePrice, Date_time) VALUES (%s,%s,%s)",(v_symbol, v_closePrice, v_Datetime))
    mydb.commit()
#def variable_table_day(v_symbol,v_closePrice,v_Datetime):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO stock_details_interval_minute (symbol, closePrice, Date_time) VALUES (%s,%s,%s)",(v_symbol, v_closePrice, v_Datetime))
    mydb.commit()


#stocks_list = ["TCS.NS", "TATASTEEL.NS", "TATAMOTORS.NS", "TITAN.NS", "TATACHEM.NS", "TATAPOWER.NS", "INDHOTEL.NS", "TATACONSUM.NS", "TATACOMM.NS", "VOLTAS.NS", "TRENT.NS", "TATASTLLP.NS", "TATAINVEST.NS", "TATAMETALI.NS", "TATAELXSI.NS", "NELCO.NS", "TATACOFFEE.NS", "TTML.NS"]
stocks_list = ["TCS.NS","TATASTEEL.NS"]

# Dataframe for RSI calculation
df = yf.download("AAPL",period= "max",interval="1d")

# Dataframe for writing data in database
df1 = yf.download(stocks_list,group_by="Ticker",period= "max",interval="1d")

df2 = df1.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
df3 = df2[["Ticker","Close","Volume"]]
#df3['Date_time'] = df3.index

df3.reset_index(level=0, inplace=True)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="stock_analysis"
)
cursor = mydb.cursor()

def RSI(df, window=14, adjust=False):
    delta = df['Close'].diff(1).dropna()
    loss = delta.copy()
    gains = delta.copy()

    gains[gains < 0] = 0
    loss[loss > 0] = 0

    gain_ewm = gains.ewm(com=window - 1, adjust=adjust).mean()
    loss_ewm = abs(loss.ewm(com=window - 1, adjust=adjust).mean())

    RS = gain_ewm / loss_ewm
    RSI = 100 - 100 / (1 + RS)

    return RSI
reversed_df = df.iloc[::-1]
df["RSI"] = talib.RSI(reversed_df["Close"])

#Insert DataFrame recrds one by one.
for i,row in df3.iterrows():

    sql = "INSERT INTO `stock_details_interval_day` (Date_time,symbol,close,volume) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))
    # the connection is not autocommitted by default, so we must commit to save our changes
    mydb.commit()