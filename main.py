from flask import Flask, render_template
from nytimesFetch import getnyt
#Get tech articles
nytimes = getnyt()

#Flask
app = Flask('app')

@app.route('/')
def hello_world():
  #for article in nytimes:
  return render_template("home.html")

app.run(host='0.0.0.0', port=8080)