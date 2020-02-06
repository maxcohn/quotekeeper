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


@bp.route('/submitquote', methods=['GET'])
def submit_quote():
    """Page that will has a form to submit quotes"""
    return render_template('submitquote.html')


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

    # add quote to list and file
    add_quote(t, a)

    return "SUCCESS"


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

def add_quote(t: str, a: str):
    """Adds a new quote to the database and local list"""

    cur = get_db().cursor()

    # insert the quote into the database
    quote.add_quote_db(cur, t, a)

    cur.close()

    # create new quote and append to all_quotes
    #all_quotes.append(Quote(t,a))



# get database from context
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE_PATH)
    return db




#DATABASE_PATH = 'main.db'