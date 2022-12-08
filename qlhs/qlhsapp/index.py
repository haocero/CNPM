from flask import render_template, request
from qlhsapp import app
import os
from qlhsapp.admin import *

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)