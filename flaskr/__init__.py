from flask import Flask, render_template, request
from nytimesFetch import getnyt

#Get tech articles
nytimes = getnyt()
page="Technology"
#Flask
app = Flask('app')

@app.route('/', methods=('GET', 'POST'))
def hello_world():
  #for article in nytimes:
  if request.method == "POST":
      print()
       # getting input with name = fname in HTML form
       #page = request.form.get("pageChoice")
       #nytimes = getnyt(page)
  return render_template("index.html", nytimes=nytimes, page=page)

app.run(host='0.0.0.0', port=8080)
