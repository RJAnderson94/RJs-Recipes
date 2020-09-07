import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cocktail_home')
def cocktail_home():
    return render_template('cocktails.html')


@app.route('/food_home')
def food_home():
    return render_template('food.html')


@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html')


@app.route('/contact_home')
def contact_home():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), port=int(
        os.environ.get('PORT')), debug=True)
