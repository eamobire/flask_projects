from flask import Flask, render_template
import random
from datetime import datetime as dt
import requests

app = Flask(__name__)


@app.route("/")
def home():
    year = dt.now().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    gender_response = requests.get(f"https://api.genderize.io/?name={name}")
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("api.html", username=name, guess_age=age, guess_gender=gender)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/0066a3f539090a5abe69"
    response = requests.get(blog_url)
    all_blog_posts = response.json()
    return render_template("blog.html",posts=all_blog_posts)



if __name__ == "__main__":
    app.run(debug=True)
