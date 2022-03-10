import yfinance as yf
import mysql.connector
from mysql.connector import Error
import pandas as pd
import time
from datetime import datetime

#msft = yf.Ticker("MSFT")
#inform=msft.info
#symbol = inform['symbol']
#shortName = inform['shortName']
#sector = inform['sector']
#country = inform['country']
#currentPrice = inform['currentPrice']


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

def variable_table(v_symbol,v_currentPrice,v_dt_string):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO stock_details_variable (symbol, currentPrice, Date_time) VALUES (%s,%s,%s)",(v_symbol,v_currentPrice,v_dt_string))
    mydb.commit()


stocks_list = ["TCS.NS", "TATASTEEL.NS", "TATAMOTORS.NS", "TITAN.NS", "TATACHEM.NS", "TATAPOWER.NS", "INDHOTEL.NS", "TATACONSUM.NS", "TATACOMM.NS", "VOLTAS.NS", "TRENT.NS", "TATASTLLP.NS", "TATAINVEST.NS", "TATAMETALI.NS", "TATAELXSI.NS", "NELCO.NS", "TATACOFFEE.NS", "TTML.NS"]

# tickers = yf.Tickers(stocks_list)
# for stock in stocks_list:
#     print(tickers.tickers[stock.upper()].info)
tickers = yf.Tickers(['MSFT','GOOG','AAPL'])
print(tickers.tickers['MSFT'].info)
print(tickers.tickers['GOOG'].info)
#print(tickers.tickers.get('MSFT').info)

# symbol = info.get('symbol')
# shortName = info.get('shortName')
# sector = info.get('sector')
# country = info.get('country')
# currentPrice = info.get('currentPrice')
#
# # datetime object containing current date and time
# now = datetime.now()
# # dd/mm/YY H:M:S
# dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
# print("date_time =", dt_string)
# print("date_time =", dt_string)
# print("date_time =", dt_string)
# variable_table(symbol, currentPrice, dt_string)

    #static_table(symbol,shortName,sector,country)

