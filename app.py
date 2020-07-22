from flask import Flask,render_template
app=Flask(__name__)

@app.before_request
def before_request():
    app.jinja_env.cache = {}

@app.route("/")
def index():
    return render_template("leaderboard.html")

if __name__ == '__main__':
    app.run()