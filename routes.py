from app import app
import visited_restaurants, bucketlist_restaurants
from flask import render_template, request, redirect

@app.route("/")
def index():
    visited_list = visited_restaurants.get_list()
    bucketlist_list = bucketlist_restaurants.get_list()
    return render_template("index.html", visited_restaurants=visited_list, bucketlist_restaurants=bucketlist_list)

@app.route("/deleted_entries")
def get_deleted_entries():
    visited_deleted_list = visited_restaurants.get_deleted_entries()
    bucketlist_deleted_list = bucketlist_restaurants.get_deleted_entries()
    return render_template("deleted_entries.html", visited_restaurants=visited_deleted_list, bucketlist_restaurants=bucketlist_deleted_list)

@app.route("/create_bucketlist_entry")
def create_bucketlist():
    return render_template("create_bucketlist_entry.html")

@app.route("/create_visited_entry")
def create_visited():
    return render_template("create_visited_entry.html")

@app.route("/bucketlist_restaurant/<int:id>/delete")
def delete_bucketlist_restaurant(id):
    bucketlist_restaurants.delete(id)
    return redirect("/")

@app.route("/bucketlist_restaurant/<int:id>/restore")
def restore_bucketlist_restaurant(id):
    bucketlist_restaurants.restore(id)
    return redirect("/")

@app.route("/visited_restaurant/<int:id>/restore")
def restore_visited_restaurant(id):
    visited_restaurants.restore(id)
    return redirect("/")

@app.route("/visited_restaurant/<int:id>/delete")
def delete_visited_restaurant(id):
    visited_restaurants.delete(id)
    return redirect("/")

@app.route("/send_visited_entry", methods=["POST"])
def send_visited_entry():
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    rating = request.form["rating"]
    review = request.form["review"]
    address = request.form["address"]
    if visited_restaurants.create(name, description, category, rating, review, address):
        return redirect("/")
    else:
        return render_template("error.html", message="Error with creating visited restaurant entry. Please try again. If issue persists, contact site maintainer. Error code: CREATION_ERROR_VISITED")

@app.route("/send_bucketlist_entry", methods=["POST"])
def send_bucketlist_entry():
    name = request.form["name"]
    description = request.form["description"]
    category = request.form["category"]
    address = request.form["address"]
    if bucketlist_restaurants.create(name, description, category, address):
       return redirect("/")
    else:
        return render_template("error.html", message="Error with creating bucketlist restaurant. Please try again. If issue persists, please contact site maintainer. Error code: CREATION_ERROR_BUCKETLIST")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/result", methods=["GET"])
def result():
    query = request.args["query"]
    visited_list = visited_restaurants.search(query)
    bucketlist_list = bucketlist_restaurants.search(query)
    return render_template("result.html", query=query, visited_restaurants=visited_list, bucketlist_restaurants=bucketlist_list)

@app.route("/bucketlist_restaurant/<int:id>")
def bucketlist_restaurant(id):
    content = bucketlist_restaurants.get_content(id)
    return render_template("bucketlist_restaurant.html", id=id, content=content)

@app.route("/visited_restaurant/<int:id>")
def visited_restaurant(id):
    content = visited_restaurants.get_content(id)
    return render_template("visited_restaurant.html", id=id, content=content)

