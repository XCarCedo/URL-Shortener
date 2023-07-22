from pathlib import Path

from flask import Flask, render_template, request
from models import db

DB_FILE = "main.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"

db.init_app(app)

@app.route("/")
def home_page():
	return render_template("home.html")

@app.route("/submit_url", methods=["POST"])
def submit_url():
	submitted_url = request.form.get("url")
	if submitted_url:
		
		return render_template("success.html")
	else:
		return render_template("error.html", error_message="Invalid request payload, please try again.")

if __name__ == "__main__":
	if not Path(f"instance/{DB_FILE}").exists():
		with app.app_context():
			db.create_all()
	app.run(debug = True)