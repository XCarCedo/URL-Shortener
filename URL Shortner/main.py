from flask import Flask, render_template, request

app = Flask(__name__)

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
	app.run(debug = True)