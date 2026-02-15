from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "<h2>Hello Vikas bhai 😄</h2><a href='/'>Back</a>"

@app.route("/about")
def about():
    return "<h3>This app is built using Python + Flask + Android WebView 🚀</h3><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
