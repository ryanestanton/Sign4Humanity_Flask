from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    title = "Home"
    return render_template('home.html', title=title)

@app.route("/about")
def about():
    title = "Home"
    return render_template('about.html', title=title)

@app.route("/signs")
def signs():
    title = "Home"
    return render_template('signs.html', title=title)

@app.route("/tutorial")
def tutorial():
    title = "Home"
    return render_template('tutorial.html', title=title)