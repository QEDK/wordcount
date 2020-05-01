from flask import Flask, render_template, request
from flask_talisman import Talisman
import re

app = Flask(__name__)
csp = {
	"default-src": "'self'",
	"style-src": ["'self'", "https://fonts.googleapis.com"],
	"font-src": "https://fonts.gstatic.com"
}
talisman = Talisman(app, content_security_policy=csp)


@app.route("/", methods=["GET", "POST"])
def home():
	text = None
	wordcount = 0
	linecount = 0
	charcount = 0
	if request.method == "POST":
		text = request.form["wordcount"]
		charcount = len(text)
		if charcount == 0:
			pass
		else:
			charcount = len(re.split(r"[^\n\r]", text)) - 1
			wordcount = len(re.split(r"\w\b", text)) - 1
			linecount = text.count("\n") + 1
	return render_template("index.html", text=text, wordcount=wordcount, charcount=charcount, linecount=linecount)


if __name__ == "__main__":
	app.debug = False
	app.run()
