from flask import Flask, redirect, render_template

import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return redirect("/static/Index.html")

@app.route("/demo")
def demo():
    return(render_template("demo.html",name="Demonstratio",n=12))

@app.route("/anon")
def anon():
    return(render_template("demo.html", name=None, n=0))

@app.route("/map")
def get_map():
    growth = get_data.get_growth_table()
    return(render_template("map.html", growth=growth))