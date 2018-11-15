from flask import Flask
from flask import render_template
from database import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)


@app.route('/cats/<int:id>')
def cat_profile(id):
    cat = get_cat(id)
    return render_template("cat.html", cat=cat)

if __name__ == '__main__':
   app.run(debug = True)
