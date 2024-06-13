from app import app
from flask import render_template, request, redirect
import restaurants
import users

@app.route("/")
def index():
	restaurants_list = restaurants.get_list()
	return render_template("index.html", restaurants=restaurants_list)

@app.route("/deleted_entries")
def get_deleted_entries():
	deleted_restaurants_list = restaurants.get_deleted_entries()
	return render_template("deleted_entries.html", restaurants=deleted_restaurants_list)

@app.route("/create", methods=["GET", "POST"])
def create_restaurant():
	if request.method == "GET":
		return render_template("create.html")

	if request.method == "POST":
		name = request.form["name"]
		if len(name) < 1 or len(name) > 25:
			return render_template("error.html", errorcode=1, message="Nimen tulee olla 1-25 merkkiä pitkä")

		description = request.form["description"]
		if len(description) < 1 or len(description) > 100:
			return render_template("error.html", errorcode=1, message="Kuvauksen tulee olla 1-100 merkkiä pitkä")

		category = request.form["category"]
		if len(category) < 1 or len(category) > 25:
			return render_template("error.html", errorcode = 1, message="Kategorian tulee olla 1-25 merkkiä pitkä")

		address = request.form["address"]
		if len(address) < 1 or len(address) > 50:
			return render_template("error.html", errorcode = 1, message="Osoitteen tulee olla 1-50 merkkiä pitkä")

		business_hours = request.form["business_hours"]
		if len(business_hours) < 1 or len(business_hours) > 50:
			return render_template("error.html", errorcode = 1, message="Osoitteen tulee olla 1-50 merkkiä pitkä")

		entry_type = request.form["entry_type"]
		if entry_type not in ("bucketlist", "visited"):
			return render_template("error.html", errorcode = 1, message="Virhe ravintolakirjauksen tyypin määrittelyssä")

		restaurant_id = restaurants.create(name, description, category, address, business_hours, entry_type)
		return redirect("/restaurant/"+str(restaurant_id))

@app.route("/restaurant/<int:id>/delete")
def delete_restaurant(id):
	restaurants.delete(id)
	return redirect("/")

@app.route("/restaurant/<int:id>/restore")
def restore_restaurant(id):
	restaurants.restore(id)
	return redirect("/")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/result", methods=["GET"])
def result():
    query = request.args["query"]
    result_list = restaurants.search(query)
    return render_template("result.html", query=query, restaurants=result_list)

@app.route("/restaurant/<int:id>")
def view_restaurant(id):
    content = restaurants.get_content(id)
    return render_template("restaurant.html", id=id, content=content)


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]

	if users.login(username, password):
		return redirect("/")
	else:
		return render_template("error.html", errorcode = 2, message="Kirjautuminen epäonnistui. Tarkista käyttäjänimi ja salasana")

@app.route("/logout")
def logout():
	users.logout()
	return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	if request.method == "POST":
		username = request.form["username"]
		if len(username) < 1 or len(username) > 20:
			return render_template("error.html", errorcode = 0,  message="Käyttäjänimen tulee olla 1-20 merkkiä pitkä")

		password = request.form["password"]
		password_verify = request.form["password_verify"]
		if password != password_verify:
			return render_template("error.html", errorcode = 0, message="Annetut salasanat eivät vastaa toisiaan")
		if password == "":
			return render_template("error.html", errorcode = 0, message="Annettu salasana ei voi olla tyhjä")

		seclevel = request.form["seclevel"]
		if seclevel != "1" or seclevel != "2":
			return render_template("error.html", errorcode = 0, message="Annettua käyttäjätasoa ei ole olemassa")

		if users.register(username, password, seclevel):
			return redirect("/")
		else:
			return render_template("error.html", errorcode = 0, message="Käyttäjän luonti epäonnistui")

