# module 10 - Flask Application
# Ella Zaputil 10/28/2025

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!!"

@app.route("/about")
def about():
    return "This is Ella's about page."

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5002, debug=True)