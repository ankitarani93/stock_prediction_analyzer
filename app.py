from flask import Flask , request, render_template
from stock_functions import print_database, findstockname, get_stock_symbols, find_stock_price
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

app = Flask(__name__)

@app.route('/line')
def line():
    labels = [
        'JAN', 'FEB', 'MAR', 'APR',
        'MAY', 'JUN', 'JUL', 'AUG',
        'SEP', 'OCT', 'NOV', 'DEC'
    ]

    values = [
        967.67, 1190.89, 1079.75, 1349.19,
        2328.91, 2504.28, 2873.83, 4764.87,
        4349.29, 6458.30, 9907, 16297
    ]

    line_labels=labels
    line_values=values
    return render_template('line_chart.html', title='Stock Price', max=17000, labels=line_labels, values=line_values)

@app.route("/", methods =["GET", "POST"])
def home():
    data = print_database()
    return render_template("table.html", data=data)

@app.route("/search", methods =["GET", "POST"])
def search():
    if request.method == "POST":
        stock_symbol = request.form['stock_drop_down']

        if request.form['submit_button'] == 'Check Price':
            # check price wala function
            data = find_stock_price(stock_symbol)
            df = pd.DataFrame(data, columns=['Date_time', 'Symbol', 'Price', 'Volume'])

            date_time_list = df['Date_time'].to_list()
            price_list = df['Price'].to_list()
            max = 4000
            line_labels=date_time_list
            line_values =price_list
            return render_template('line_chart.html', title=stock_symbol, max=max, labels=line_labels,
                                   values=line_values)
            #return render_template("table.html", data=data)

        if request.form['submit_button'] == 'Check RSI':
            # RSI wala function
            data = find_stock_price(stock_symbol)
            return render_template("table.html", data=data)

    list_of_symbols = get_stock_symbols()
    return render_template("formcheck.html",stocks_list=list_of_symbols)
