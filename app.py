# module 10 - Flask Application
# Ella Zaputil 10/28/2025

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5002, debug=True)