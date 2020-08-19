from app import app
import requests
from flask import render_template, url_for

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate")
def generate():
    response = requests.get("http://localhost:5001/api/animal")
    response = response.text

    response2 = requests.post("http://localhost:5001/api/animal/noise", data = response)
    response2 = response2.text

    return (response + " " + response2)