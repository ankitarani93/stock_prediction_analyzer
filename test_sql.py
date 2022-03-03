import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="world"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM city")

myresult = mycursor.fetchall()
df = pd.DataFrame(myresult)
print(df)
