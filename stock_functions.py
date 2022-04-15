from flask import request, render_template
import mysql.connector

def print_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM stock_details_interval_minute")
    myresult = (mycursor.fetchall())
    return myresult

def findstockname():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        symbol = request.form.get("Stockname")

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",
            database="stock_analysis"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM stock_details_interval_minute where symbol = %s", (symbol,))
        myresult = (mycursor.fetchall())
        return myresult

    return render_template("formcheck.html")

def get_stock_symbols():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT distinct symbol FROM stock_details_interval_minute")
    myresult = (mycursor.fetchall())

    list_symbol = []
    for item_tuple in myresult:
        for item in item_tuple:
            list_symbol.append(item)
    return list_symbol

def find_stock_price(stock_symbol):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="stock_analysis"
    )

    stock_symbol_list = []
    stock_symbol_list.append(stock_symbol)

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM stock_details_interval_minute where symbol = %s",stock_symbol_list)
    myresult = (mycursor.fetchall())
    return myresult
