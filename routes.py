from app import app
import restaurants
from flask import render_template, request, redirect

@app.route("/")
def index():
    list = restaurants.get_list()
    return render_template("index.html", Restaurants=list)

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/send", methods=["POST"])
def send():
    name = request.form["name"]
    description = request.form["description"]
    if restaurants.create(name, description):
        return redirect("/")
    else:
        return render_template("error.html", message="Error with creating restaurant")

