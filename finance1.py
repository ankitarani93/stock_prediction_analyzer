import yfinance as yf
import mysql.connector
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


stocks_list = ["TCS.NS", "TATASTEEL.NS", "TATAMOTORS.NS", "TITAN.NS", "TATACHEM.NS", "TATAPOWER.NS", "INDHOTEL.NS", "TATACONSUM.NS", "TATACOMM.NS", "VOLTAS.NS", "TRENT.NS", "TATASTLLP.NS", "TATAINVEST.NS", "TATAMETALI.NS", "TATAELXSI.NS", "NELCO.NS", "TATACOFFEE.NS", "TTML.NS"]

#df1 = yf.download("AAPL SPY",group_by="Ticker",period= "1d",interval="1m")
df1 = yf.download(stocks_list,group_by="Ticker",period= "7d",interval="1m")

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

# Insert DataFrame recrds one by one.
for i,row in df3.iterrows():
    # print("i= ",i)
    # print("row=",type(row[0]))
    #
    # row.update(pd.Series([row[0].tz_convert(None)], index=[0]))
    # print(row[0])
    sql = "INSERT INTO `stock_details_variable` (Date_time,symbol,close,volume) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

    # the connection is not autocommitted by default, so we must commit to save our changes
    mydb.commit()

