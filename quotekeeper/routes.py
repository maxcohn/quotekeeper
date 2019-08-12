from flask import Blueprint, request, render_template
import os
import random
import sys
import re

# learned something here: need to specify current package if wanting
# to import a module from current package (using relative imports here)
from .quote import Quote
from . import quote


bp = Blueprint('routes', __name__)

# read in all quotes from the file
all_quotes = quote.all_quotes()



"""Home page that displays quotes. The page lists all quotes and their authors.
"""
@bp.route('/', methods=['GET'])
def home():
    # TODO maybe randomize whole list instead of making new one??
    randomized_quotes = [q for q in all_quotes]
    random.shuffle(randomized_quotes)
    return render_template('base.html', quotes=randomized_quotes)


@bp.route('/submitquote', methods=['GET'])
def submitequote():
    return render_template('submitquote.html')


@bp.route('/newquote', methods=['POST'])
def new_quote():
    """URL to post to to add a new quote. Format of JSON is:
    
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

    return "return" #TODO remove this


@bp.route('/filter/name/<name>', methods=['GET'])
def filter_name(name):
    return render_template('base.html', quotes=quote.filter_quote_name(name))

@bp.route('/filter/text/<text>', methods=['GET'])
def filter_text(text):
    return render_template('base.html', quotes=quote.filter_quote_text(text))

def add_quote(t: str, a: str):
    print(f'New quote: {t}\nSaid by: {a}', file=sys.stderr)
    
    # insert the quote into the database
    quote.add_quote_db(t, a)

    # create new quote and append to all_quotes
    all_quotes.append(Quote(t,a))

