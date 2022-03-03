from flask import Flask , request, render_template
import mysql.connector
#import psycopg2
import pandas as pd


app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
def print_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="world"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM city")
    myresult = (mycursor.fetchall())
    #return str(myresult)
    return render_template("table.html", data=myresult)

@app.route("/search", methods =["GET", "POST"])
def findcityname():
        if request.method == "POST":
            # getting input with name = fname in HTML form
            cityname = request.form.get("Cityname")

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="world"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM city where Name = %s", (cityname,))
            myresult = (mycursor.fetchall())
            return render_template("table.html", data=myresult)


        return render_template("formcheck.html")