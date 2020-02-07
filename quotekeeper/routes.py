from flask import Blueprint, request, render_template, g
import os
import random
import sys
import re
import sqlite3

# learned something here: need to specify current package if wanting
# to import a module from current package (using relative imports here)
from .quote import Quote
from . import quote

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "quotes.db")

bp = Blueprint('routes', __name__)

# read in all quotes from the file

@bp.route('/', methods=['GET'])
def home():
    """
    Home Page

    Renders a page with all quotes displayed.
    """
    cur = get_db().cursor()
    all_quotes = quote.all_quotes(cur)
    cur.close()

    random.shuffle(all_quotes)
    return render_template('base.html', quotes=all_quotes)


@bp.route('/new', methods=['GET'])
def submit_quote():
    """Page that will has a form to submit quotes"""
    return render_template('new.html')


@bp.route('/newquote', methods=['POST'])
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
    quote.add_quote_db(cur, t, a)
    cur.close()
    get_db().commit()

    return ""


@bp.route('/filter/name/<name>', methods=['GET'])
def filter_name(name):
    """
    Renders home page, but filters quotes that contain `name` in the `author`
    section
    """
    cur = get_db().cursor()
    quotes = quote.filter_quote_name(cur, name)
    cur.close()
    return render_template('base.html', quotes=quotes)

@bp.route('/filter/text/<text>', methods=['GET'])
def filter_text(text):
    """
    Renders home page, but filters quotes that contain `text` in the `quote`
    section
    """

    cur = get_db().cursor()

    quotes = quote.filter_quote_text(cur, text)

    cur.close()
    return render_template('base.html', quotes=quotes)



# get database from context
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_PATH)
    return db




#DATABASE_PATH = 'main.db'