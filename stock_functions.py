from flask import request, render_template

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
    return render_template("table.html", data=myresult)

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
        return render_template("table.html", data=myresult)

    return render_template("formcheck.html")