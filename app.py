from flask import Flask, render_template, flash
app=Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


@app.before_request
def before_request():
    app.jinja_env.cache = {}

@app.route("/")
def index():
    return render_template("leaderboard.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html")

@app.errorhandler(403)
def noAccess(e):
    return render_template("error/403.html")

@app.route("/testLogin/")
def login():
    flash("lol testing!")
    return render_template("login.html")

if __name__ == '__main__':
    app.run()