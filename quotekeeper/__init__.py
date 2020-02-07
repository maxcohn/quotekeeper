import os
import sqlite3
from flask import Flask, request, render_template, g
from . import db
import random

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "quotes.db")

# read in all quotes from the file
@app.route('/', methods=['GET'])
def home():
    """
    Home Page

    Renders a page with all quotes displayed.
    """
    cur = get_db().cursor()
    all_quotes = db.all_quotes(cur)
    cur.close()

    random.shuffle(all_quotes)
    return render_template('base.html', quotes=all_quotes)


@app.route('/new', methods=['GET'])
def submit_quote():
    """Page that will has a form to submit quotes"""
    return render_template('new.html')


@app.route('/newquote', methods=['POST'])
def new_quote():
    """
    URL to post to to add a new quote. Format of JSON is:
    
    {
        text:'',
        author:''
    }

    On receiving a request, we append the new quote onto all_quotes and then
    append the new quote to the file that stores them (quotes.txt)
    """
    data = request.get_json()

    # extract text and author
    t = data['text']
    a = data['author']

    print(f'{t}, said by {a}', flush=True)

    # insert the quote into the database
    cur = get_db().cursor()
    db.add_quote_db(cur, t, a)
    cur.close()
    get_db().commit()

    return ""


@app.route('/filter/name/<name>', methods=['GET'])
def filter_name(name):
    """
    Renders home page, but filters quotes that contain `name` in the `author`
    section
    """
    cur = get_db().cursor()
    quotes = db.filter_quote_name(cur, name)
    cur.close()
    return render_template('base.html', quotes=quotes)

@app.route('/filter/text/<text>', methods=['GET'])
def filter_text(text):
    """
    Renders home page, but filters quotes that contain `text` in the `quote`
    section
    """

    cur = get_db().cursor()

    quotes = db.filter_quote_text(cur, text)

    cur.close()
    return render_template('base.html', quotes=quotes)



# get database from context
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_PATH)
    return db

# destroy database
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



#DATABASE_PATH = 'main.db'

if __name__ == '__main__':
    app.run()