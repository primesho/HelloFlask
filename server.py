# coding: utf-8
from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()