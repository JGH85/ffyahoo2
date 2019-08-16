# 1. import Flask
from flask import Flask
import logic
import team, game, league, yhandler
from yahoo_oauth import OAuth2

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


sc = OAuth2(None, None, from_file='oauth2.json')
kffl_league_id = '390.l.707700'

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    currentteam = logic.CurrentUserTeam()
    text = f"Welcome to The Troy Siade Dynasty Fantasy Football League! " \
           f"Your team:  {currentteam.teamname}. " \
           f"Manager:  {currentteam.managernickname}."
    print(f"Current Team: {currentteam.teamname}")
    print(f"CUrrent Manager: {currentteam.managernickname}")
    return text


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
    app.run(debug=True)
