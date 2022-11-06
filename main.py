# imports the module
from flask import Flask, render_template, request, redirect, g, url_for
from flask import render_template
import json
# variable to hold the URL for the web application
app = Flask(__name__)


@app.route("/")
def home(name=None):
  return render_template('index.html', name=name)


# function to handle the web requests
#@app.route("/<name>")
#def name():
#return f"Hello {name}"

# function uses HTTP request that allows us to retrieve data from forms on our web page.
#@app.route("/login", methods=["GET", "POST"])
#def login():
#if #METHOD# == "GET":
# display the /login.html form
# have some code for the submit button that submits a post requests
#elif #METHOD# == "POST":
# retrieves the data from the form
#username = request.form.get("username")
#password = request.form.get("password")
# check username and password are right
# returns the data to the user
#return f"Welcome {username}"

# function uses "questions.html" to ask the user questions

if __name__ == "__main__":
  app.run(host='0.0.0.0')