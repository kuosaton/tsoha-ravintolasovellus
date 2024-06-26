from app import app
from flask import render_template, request, redirect
import restaurants
import users
import reviews

@app.errorhandler(404)
def not_found(e):
	return render_template("error.html", errorcode=404, message=e)

@app.route("/")
def index():
	restaurants_list = restaurants.get_list()
	return render_template("index.html", restaurants=restaurants_list)

@app.route("/create", methods=["GET", "POST"])
def create_restaurant():
	users.check_seclevel(1)

	if request.method == "GET":
		return render_template("create.html")

	if request.method == "POST":
		users.check_csrf()

		name = request.form["name"]
		if len(name) < 1 or len(name) > 50:
			return render_template("error.html", errorcode=1, message="Nimi voi olla 1-50 merkkiä pitkä")

		description = request.form["description"]
		if len(description) < 1 or len(description) > 1000:
			return render_template("error.html", errorcode=1, message="Kuvaus voi olla 1-1000 merkkiä pitkä")

		category = request.form["category"]
		if len(category) < 1 or len(category) > 30:
			return render_template("error.html", errorcode = 1, message="Kategoria voi olla 1-30 merkkiä pitkä")

		address = request.form["address"]
		if address == "":
			address = "-"
		elif len(address) > 50:
			return render_template("error.html", errorcode = 1, message="Osoite voi olla 1-50 merkkiä pitkä")

		business_hours = request.form["business_hours"]
		if business_hours == "":
			business_hours = "-"
		elif len(business_hours) > 1000:
			return render_template("error.html", errorcode = 1, message="Aukioloajat voivat olla 1-1000 merkkiä pitkät")

		entry_type = request.form["entry_type"]
		if entry_type not in ("1", "2"):
			return render_template("error.html", errorcode = 1, message="Virhe ravintolakirjauksen tyypin määrittelyssä")

		restaurant_id = restaurants.create(name, description, category, address, business_hours, entry_type)
		return redirect("/restaurant/"+str(restaurant_id))

@app.route("/delete_restaurant", methods = ["GET", "POST"])
def delete_restaurant():
	users.check_seclevel(2)

	if request.method == "GET":
		restaurants_list = restaurants.get_list()
		return render_template("delete_restaurant.html", restaurants=restaurants_list)

	if request.method == "POST":
		users.check_csrf()
		if "restaurant" in request.form:
			restaurant_id = request.form["restaurant"]
			restaurants.delete(restaurant_id)

		return redirect("/")

@app.route("/restore_restaurant", methods = ["GET", "POST"])
def restore_restaurant():
	users.check_seclevel(2)

	if request.method == "GET":
		deleted_restaurants = restaurants.get_deleted_entries()
		return render_template("restore_restaurant.html", restaurants=deleted_restaurants)

	if request.method == "POST":
		users.check_csrf()
		if "restaurant" in request.form:
			restaurant_id = request.form["restaurant"]
			restaurants.restore(restaurant_id)

		return redirect("/")

@app.route("/delete_review", methods = ["GET", "POST"])
def delete_review():
	users.check_seclevel(2)

	if request.method == "GET":
		reviews_list = reviews.get_list()
		return render_template("delete_review.html", reviews=reviews_list)

	if request.method == "POST":
		users.check_csrf()
		if "review" in request.form:
			review_id = request.form["review"]
			reviews.delete(review_id)

		return redirect("/")

@app.route("/restore_review", methods = ["GET", "POST"])
def restore_review():
	users.check_seclevel(2)
	if request.method == "GET":
		deleted_reviews = reviews.get_deleted_entries()
		return render_template("restore_review.html", reviews=deleted_reviews)

	if request.method == "POST":
		users.check_csrf()
		if "review" in request.form:
			review_id = request.form["review"]
			reviews.restore(review_id)

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
	restaurant = restaurants.get_content(id)
	reviews_list = reviews.get_content(id)
	rating = reviews.get_rating_average(id)
	return render_template("restaurant.html", id=id, rating=rating, restaurant=restaurant, reviews=reviews_list)


@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]

	if not users.login(username, password):
		return render_template("error.html", errorcode = 2, message="Kirjautuminen epäonnistui. Tarkista käyttäjänimi ja salasana")

	return redirect("/")

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
		if len(username) < 1 or len(username) > 30:
			return render_template("error.html", errorcode = 0,  message="Käyttäjänimi voi olla 1-30 merkkiä pitkä")

		password = request.form["password"]
		password_verify = request.form["password_verify"]

		if password != password_verify:
			return render_template("error.html", errorcode = 0, message="Annetut salasanat eivät vastaa toisiaan")
		if len(password) < 1 or len(password) > 30:
			return render_template("error.html", errorcode = 0, message="Salasana voi olla 1-30 merkkiä pitkä")

		seclevel = request.form["seclevel"]

		if seclevel not in ("1", "2"):
			return render_template("error.html", errorcode = 0, message="Annettua käyttäjätasoa ei ole olemassa")

		if not users.register(username, password, seclevel):
			return render_template("error.html", errorcode = 0, message="Tietojen tallentaminen ei onnistunut.")

		return redirect("/")

@app.route("/restaurant/<int:id>/create_review", methods=["GET", "POST"])
def create_review(id):
	users.check_seclevel(1)

	if request.method == "GET":
		return render_template("create_review.html", id=id)

	if request.method == "POST":
		users.check_csrf()

		title = request.form["title"]
		if len(title) < 1 or len(title) > 50:
			return render_template("error.html", errorcode = 3, message="Arvostelun otsikko voi olla 1-30 merkkiä pitkä")

		description = request.form["description"]
		if len(description) < 1 or len(description) > 1000:
			return render_template("error.html", errorcode = 3, message="Arvostelun kuvaus voi olla 1-1000 merkkiä pitkä")

		rating = request.form["rating"]
		if rating not in ("1", "2", "3", "4", "5"):
			return render_template("error.html", errorcode = 3, message="Arvostelun annettu arviosyöte (tähdet) oli virheellinen")

		recommendation = request.form["recommendation"]
		if recommendation not in ("1", "2"):
			return render_template("error.html", errorcode = 3, message="Arvostelun annettu suosittelusyöte oli virheellinen")

		user_id = request.form["user_id"]

		user_name = request.form["user_name"]


		if not reviews.create(id, user_id, user_name, title, description, rating, recommendation):
			return render_template("error.html", errorcode = 3, message="Arvostelun tallentamisessa tapahtui virhe")

		return redirect("/restaurant/"+str(id))
