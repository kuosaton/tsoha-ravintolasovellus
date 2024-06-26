from app import app
from flask import render_template, request, redirect
import restaurants
import users
import reviews
import questions
import answers

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
			return render_template("error.html", errorcode = 1, message="Nimi voi olla 1-50 merkkiä pitkä.")

		description = request.form["description"]
		if len(description) < 1 or len(description) > 1000:
			return render_template("error.html", errorcode = 1, message="Kuvaus voi olla 1-1000 merkkiä pitkä.")

		category = request.form["category"]
		if len(category) < 1 or len(category) > 30:
			return render_template("error.html", errorcode = 1, message="Kategoria voi olla 1-30 merkkiä pitkä.")

		address = request.form["address"]
		if address == "":
			address = "-"
		elif len(address) > 100:
			return render_template("error.html", errorcode = 1, message="Yhteystiedot voivat olla 1-100 merkkiä pitkät.")

		business_hours = request.form["business_hours"]
		if business_hours == "":
			business_hours = "-"
		elif len(business_hours) > 1000:
			return render_template("error.html", errorcode = 1, message="Aukioloajat voivat olla 1-1000 merkkiä pitkät.")

		entry_type = request.form["entry_type"]
		if entry_type not in ("1", "2"):
			return render_template("error.html", errorcode = 1, message="Annettu kirjaustyyppi oli virheellinen.")

		restaurant_id = restaurants.create(name, description, category, address, business_hours, entry_type)
		return redirect("/restaurant/"+str(restaurant_id))

@app.route("/restaurant/<int:id>/edit", methods = ["GET", "POST"])
def edit_restaurant(id):
	users.check_seclevel(2)

	if request.method == "GET":
		restaurant_content = restaurants.get_content(id)
		return render_template("edit_restaurant.html", id = id, restaurant = restaurant_content)

	if request.method == "POST":
		users.check_csrf()

		name = request.form["name"]
		if len(name) < 1 or len(name) > 50:
			return render_template("error.html", errorcode = 7, message="Nimi voi olla 1-50 merkkiä pitkä.")

		description = request.form["description"]
		if len(description) < 1 or len(description) > 1000:
			return render_template("error.html", errorcode = 7, message="Kuvaus voi olla 1-1000 merkkiä pitkä.")

		category = request.form["category"]
		if len(category) < 1 or len(category) > 30:
			return render_template("error.html", errorcode = 7, message="Kategoria voi olla 1-30 merkkiä pitkä.")

		address = request.form["address"]
		if len(address) < 1 or len(address) > 100:
			return render_template("error.html", errorcode = 7, message="Yhteystiedot voivat olla 1-100 merkkiä pitkät.")

		business_hours = request.form["business_hours"]
		if len(business_hours) < 1 or len(business_hours) > 1000:
			return render_template("error.html", errorcode = 7, message="Aukioloajat voivat olla 1-1000 merkkiä pitkät.")

		entry_type = request.form["entry_type"]
		if entry_type not in ("1", "2"):
			return render_template("error.html", errorcode = 7, message="Annettu kirjaustyyppi oli virheellinen.")

		try:
			restaurants.edit(id, name, description, category, address, business_hours, entry_type)
		except:
			return render_template("error.html", errorcode = 7, message="Ravintolan tietojen päivittäminen ei onnistunut. Tarkista annetut tiedot.")

		return redirect("/restaurant/"+str(id))

@app.route("/delete_restaurant", methods = ["GET", "POST"])
def delete_restaurant():
	users.check_seclevel(2)

	if request.method == "GET":
		restaurants_list = restaurants.get_list()
		return render_template("delete_restaurant.html", restaurants=restaurants_list)

	if request.method == "POST":
		users.check_csrf()

		if "restaurant" in request.form:
			try:
				restaurant_id = request.form["restaurant"]
				restaurants.delete(restaurant_id)
			except:
				return render_template("error.html", errorcode = 8, message="Ravintolan poistaminen epäonnistui.")

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
			try:
				restaurant_id = request.form["restaurant"]
				restaurants.restore(restaurant_id)
			except:
				return render_template("error.html", errorcode = 9, message="Ravintolan palauttaminen epäonnistui.")

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
			try:
				review_id = request.form["review"]
				reviews.delete(review_id)
			except:
				return render_template("error.html", errorcode = 8, message="Arvostelun poistaminen epäonnistui.")

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
			try:
				review_id = request.form["review"]
				reviews.restore(review_id)
			except:
				return render_template("error.html", errorcode = 9, message="Arvostelun palauttaminen epäonnistui.")

		return redirect("/")

@app.route("/delete_question", methods = ["GET", "POST"])
def delete_question():
	users.check_seclevel(2)

	if request.method == "GET":
		questions_list = questions.get_list()
		return render_template("delete_question.html", questions = questions_list)

	if request.method == "POST":
		users.check_csrf()

		if "question" in request.form:
			try:
				question_id = request.form["question"]
				questions.delete(question_id)

				answers.delete_question_answers(question_id)
			except:
				return render_template("error.html", errorcode = 8, message="Kysymyksen poistaminen epäonnistui.")

		return redirect("/")

@app.route("/restore_question", methods = ["GET", "POST"])
def restore_question():
	users.check_seclevel(2)

	if request.method == "GET":
		deleted_questions = questions.get_deleted_entries()
		return render_template("restore_question.html", questions = deleted_questions)

	if request.method == "POST":
		users.check_csrf()

		if "question" in request.form:
			try:
				question_id = request.form["question"]
				questions.restore(question_id)

				answers.restore_question_answers(question_id)
			except:
				return render_template("error.html", errorcode = 9, message="Kysymyksen palauttaminen epäonnistui.")

		return redirect("/")

@app.route("/delete_answer", methods = ["GET", "POST"])
def delete_answer():
	users.check_seclevel(2)

	if request.method == "GET":
		answers_list = answers.get_list()
		return render_template("delete_answer.html", answers = answers_list)

	if request.method == "POST":
		users.check_csrf()

		if "answer" in request.form:
			try:
				answer_id = request.form["answer"]
				question_id = request.form["question_id"]

				answers.delete(answer_id)
				questions.mark_as_unanswered(question_id)

			except:
				return render_template("error.html", errorcode = 8, message="Vastauksen poistaminen epäonnistui. Tämä voi johtua siitä, että siihen linkittyneen kysymyksen käsittelyssä tapahtui virhe.")

		return redirect("/")

@app.route("/restore_answer", methods = ["GET", "POST"])
def restore_answer():
	users.check_seclevel(2)

	if request.method == "GET":
		deleted_answers = answers.get_deleted_entries()
		return render_template("restore_answer.html", answers = deleted_answers)

	if request.method == "POST":
		users.check_csrf()

		if "answer" in request.form:
			try:
				answer_id = request.form["answer"]
				question_id = request.form["question_id"]

				answers.restore(answer_id)
				questions.mark_as_answered(question_id)

			except:
				return render_template("error.html", errorcode = 9, message="Vastauksen palauttaminen epäonnistui. Tämä voi johtua siitä, että siihen linkittyneen kysymyksen käsittelyssä tapahtui virhe.")

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
	reviews_list = reviews.get_restaurant_reviews(id)
	rating = reviews.get_rating_average(id)
	questions_list = questions.get_restaurant_questions(id)
	answers_list = []

	if questions_list:
		for question in questions_list:
			if answers.get_question_answers(question.id):
				answers_list.append(answers.get_question_answers(question.id))

	return render_template("restaurant.html", id=id, rating=rating, restaurant=restaurant, reviews=reviews_list, questions=questions_list, answers=answers_list)


@app.route("/profile", methods=["GET"])
def view_profile():
	if request.method == "GET":
		if not users.get_id():
			return render_template("error.html", errorcode = 5, message="Ei tarkasteltavaa profiilia, et ole kirjautunut sisään.")

		user_id = users.get_id()
		username = users.get_name()

		reviews_list = reviews.get_user_reviews(user_id)
		questions_list = questions.get_user_questions(user_id)
		answers_list = answers.get_user_answers(user_id)

		return render_template("profile.html", username = username, reviews = reviews_list, questions = questions_list, answers = answers_list)

@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	if request.method == "POST":
		username = request.form["username"]
		password = request.form["password"]

	if not users.login(username, password):
		return render_template("error.html", errorcode = 2, message="Tarkista käyttäjänimi ja salasana.")

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
		if len(username) < 4 or len(username) > 30:
			return render_template("error.html", errorcode = 0,  message="Käyttäjänimi voi olla 4-30 merkkiä pitkä.")

		password = request.form["password"]
		password_verify = request.form["password_verify"]

		if password != password_verify:
			return render_template("error.html", errorcode = 0, message="Annetut salasanat eivät vastaa toisiaan.")
		if len(password) < 8 or len(password) > 30:
			return render_template("error.html", errorcode = 0, message="Salasana voi olla 8-30 merkkiä pitkä.")

		seclevel = request.form["seclevel"]

		if seclevel not in ("1", "2"):
			return render_template("error.html", errorcode = 0, message="Annettua käyttäjätasoa ei ole olemassa.")

		if not users.register(username, password, seclevel):
			return render_template("error.html", errorcode = 0, message="Käyttäjätilin luonti ei onnistunut. Annettu käyttäjänimi on mahdollisesti jo käytössä.")

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
			return render_template("error.html", errorcode = 3, message="Arvostelun otsikko voi olla 1-50 merkkiä pitkä.")

		description = request.form["description"]
		if len(description) < 1 or len(description) > 1000:
			return render_template("error.html", errorcode = 3, message="Arvostelun kuvaus voi olla 1-1000 merkkiä pitkä.")

		rating = request.form["rating"]
		if rating not in ("1", "2", "3", "4", "5"):
			return render_template("error.html", errorcode = 3, message="Arvostelun annettu arviosyöte (tähdet) oli virheellinen.")

		recommendation = request.form["recommendation"]
		if recommendation not in ("1", "2"):
			return render_template("error.html", errorcode = 3, message="Arvostelun annettu suosittelusyöte oli virheellinen.")

		creator_id = request.form["creator_id"]
		creator_name = request.form["creator_name"]

		if not reviews.create(id, creator_id, creator_name, title, description, rating, recommendation):
			return render_template("error.html", errorcode = 3, message="Arvostelun tallentamisessa tapahtui virhe.")

		return redirect("/restaurant/"+str(id))

@app.route("/restaurant/<int:id>/create_question", methods=["GET", "POST"])
def create_question(id):
	users.check_seclevel(1)

	if request.method == "GET":
		return render_template("create_question.html", id=id)

	if request.method == "POST":
		users.check_csrf()

		content = request.form["content"]
		if len(content) < 1 or len(content) > 1000:
			return render_template("error.html", errorcode = 4, message="Kysymys voi olla 1-1000 merkkiä pitkä.")

		creator_id = request.form["creator_id"]
		creator_name = request.form["creator_name"]

		if not questions.create(id, creator_id, creator_name, content):
			return render_template("error.html", errorcode = 4, message="Kysymyksen luonnissa tapahtui virhe.")

		return redirect("/restaurant/"+str(id))


@app.route("/restaurant/<int:id>/create_answer", methods=["GET", "POST"])
def create_answer(id):
	users.check_seclevel(1)

	if request.method == "GET":
		questions_list = questions.get_unanswered_restaurant_questions(id)
		return render_template("create_answer.html", id=id, questions=questions_list)

	if request.method == "POST":
		users.check_csrf()

		question_id = request.form["question_id"]

		content = request.form["content"]
		if len(content) < 1 or len(content) > 1000:
			return render_template("error.html", errorcode = 6, message="Vastaus voi olla 1-1000 merkkiä pitkä.")

		creator_id = request.form["creator_id"]
		creator_name = request.form["creator_name"]

		if not answers.create(question_id, creator_id, creator_name, content):
			return render_template("error.html", errorcode = 6, message="Vastauksen luonnissa tapahtui virhe.")

		questions.mark_as_answered(question_id)

		return redirect("/restaurant/"+str(id))
