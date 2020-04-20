from flask import Flask, render_template, request
import re

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
	text = None
	wordcount = 0
	linecount = 0
	if request.method == "POST":
		text = request.form["wordcount"]
		wordcount = len(re.split(r"\w\b", text)) - 1
		linecount = len(text.split("\n"))
	return render_template("index.html", text=text, wordcount=wordcount, linecount=linecount)


if __name__ == "__main__":
	app.debug = True
	app.run(debug=True)
