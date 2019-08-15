from flask import render_template
from flask import request
from app import app
from app import plot




@app.route('/', methods=['GET'])
def index():
    return render_template("index.html", test=plot.get_data())
