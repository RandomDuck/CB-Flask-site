from flask import Flask, render_template, flash, request, url_for, session, redirect
import requests as httpReq

app=Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
CLIENT_ID=735735948956008479
CLIENT_SECRET="qpmKJ0TZQcz5wxI3n2fY7ROtuNPwoToX"
rediUrl="http%3A%2F%2Flocalhost%3A5000%2FtestLogin%2F"
oathUrl=f"https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={rediUrl}&response_type=code&scope=identify"

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

@app.route("/passre/",methods=["post"])
def passRedir():
    try:
        session['chekpointpass']=request.form["checkpointpass"]
    except Exception as e:
        print(e)
        return render_template("error/500.html", error=e)
    return redirect(oathUrl)

@app.route("/testLogin/",methods=["get","post"])
def login():
    try:
        postdata={
            "code":request.args["code"],
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": 'authorization_code',
            "redirect_uri": 'http://localhost:5000/testLogin/',
            "scope": 'identify'
        }
        x=httpReq.post("https://discord.com/api/oauth2/token",data=postdata)
        i=httpReq.get('https://discord.com/api/users/@me', headers={'Authorization': 'Bearer '+x.json()['access_token']})
        data=i.json()
        return render_template("login.html", code=f"({data['id']}) {data['username']}#{data['discriminator']}", passw=session.get('chekpointpass',None))
    except Exception as e:
        return render_template("error/500.html", error=e)

if __name__ == '__main__':
    app.run()