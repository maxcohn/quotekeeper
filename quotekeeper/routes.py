from flask import Blueprint, request, render_template
import os
import random
import sys
import re
from quotekeeper.quote import Quote

bp = Blueprint('routes', __name__)

# read in all quotes from the file
all_quotes = Quote.get_quotes() # TODO move this into __init__

"""Home page that displays quotes. The page lists all quotes and their authors.
"""
@bp.route('/', methods=['GET'])
def home():
    randomized_quotes = [q for q in all_quotes]
    random.shuffle(randomized_quotes)
    return render_template('base.html', quotes=randomized_quotes)


"""URL to post to to add a new quote. Format of JSON is:
{
    text:'',
    author:''
}

On receiving a request, we append the new quote onto all_quotes and then
append the new quote to the file that stores them (quotes.txt)
"""
@bp.route('/newquote', methods=['POST'])
def new_quote():
    data = request.get_json()

    # t = request.form['input-text']
    # a = request.form['input-author']

    # extract text and author
    t = data['text']
    a = data['author']

    print(f'New quote: {t}\nSaid by: {a}', file=sys.stderr)

    # create new quote and append to all_quotes
    all_quotes.append(Quote(t,a))

    #TODO add to quotes.txt
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "quotes.txt"))
    with open(filepath, 'a+') as f:
        f.write(f'\n{t}|{a}')

    #print(all_quotes.)
    return "return"



