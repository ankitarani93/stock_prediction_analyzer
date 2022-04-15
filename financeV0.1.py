import yfinance as yf
import mysql.connector

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

tickers = yf.Tickers(['MSFT','GOOG','AAPL'])
print(tickers.tickers['MSFT'].info)
print(tickers.tickers['GOOG'].info)

