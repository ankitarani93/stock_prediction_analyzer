import yfinance as yf
import mysql.connector
import talib
def rsi_table(v_symbol,v_closePrice,v_rsi):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO stock_rsi_indicator (symbol, closePrice, rsi) VALUES (%s,%s,%s)",(v_symbol, v_closePrice, v_rsi))
    mydb.commit()

#stocks_list = ["TCS.NS", "TATASTEEL.NS", "TATAMOTORS.NS", "TITAN.NS", "TATACHEM.NS", "TATAPOWER.NS", "INDHOTEL.NS", "TATACONSUM.NS", "TATACOMM.NS", "VOLTAS.NS", "TRENT.NS", "TATASTLLP.NS", "TATAINVEST.NS", "TATAMETALI.NS", "TATAELXSI.NS", "NELCO.NS", "TATACOFFEE.NS", "TTML.NS"]
stocks_list = ["TCS.NS","TATASTEEL.NS"]

df = yf.download("AAPL",period= "1y",interval="1d")
df1 = yf.download(stocks_list,group_by="Ticker",period= "1y",interval="1d")
df2 = df1.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
df3 = df2[["Ticker","Close","Volume"]]

df3.reset_index(level=0, inplace=True)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="stock_analysis"
)
cursor = mydb.cursor()

def RSI(df1, window=14, adjust=False):
    delta = df1['Close'].diff(1).dropna()
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
df["RSI"] = talib.RSI(reversed_df["Close"], 14)
print(df["RSI"] )