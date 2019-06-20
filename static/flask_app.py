from flask import Flask, redirect,render_template


app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/static/Index.html")

@app.route("/demo")
def demo():
    return (render_template("hello.html"))