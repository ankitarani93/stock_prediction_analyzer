from flask import Flask
from stock_functions import print_database, findstockname

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])
print_database()

@app.route("/search", methods =["GET", "POST"])
findstockname()