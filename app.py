"""App"""

from flask import Flask, render_template
from requests import get

# ???

app = Flask(__name__)
URL = "https://my-json-server.typicode.com/jjjosephhh/test-db-002/people"

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/jobs")
def jobs():
    data = get(URL)
    return render_template("details.html", data=data.json())

if __name__ == '__main__':
    app.run("0.0.0.0", 5000, debug=True, threaded=True)
