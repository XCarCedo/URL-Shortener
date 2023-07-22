from pathlib import Path

from flask import Flask, render_template, request, redirect
from models import db, URL
from utils import generate_id

DB_FILE = "main.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"

db.init_app(app)

@app.route("/", methods=["GET"])
def home_page():
	return render_template("home.html")

@app.route("/submit_url", methods=["POST"])
def submit_url():
	submitted_url = request.form.get("url")
	if submitted_url:
		link_id = generate_id()

		db.session.add(URL(id = link_id, url=submitted_url))
		db.session.commit()
		
		return render_template("success.html", shortend_url=f"{request.host_url}redirect?id={link_id}")
	else:
		return render_template("error.html", error_message="Invalid request payload, please try again.")

@app.route("/redirect", methods=["GET"])
def redirect_page():
	_id = request.args.get("id")
	if _id:
		requested_url = URL.query.get_or_404(_id)
		return redirect(requested_url.url)
	else:
		return render_template("error.html", error_message="Invalid url, check your link.")

if __name__ == "__main__":
	if not Path(f"instance/{DB_FILE}").exists():
		with app.app_context():
			db.create_all()
	app.run(debug = True)