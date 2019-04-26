from flask import Blueprint, request, render_template
from os import path
import sys
import re
from quotekeeper.quote import Quote

bp = Blueprint('routes', __name__)

# read in all quotes from the file
all_quotes = Quote.get_quotes()

"""Home page that displays quotes. The page lists all quotes and their authors.
"""
@bp.route('/', methods=['GET'])
def home(): 
    return render_template('base.html', quotes=all_quotes)


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

    # extract text and author
    t = data['text']
    a = data['author']

    print(f'New quote: {t}\nSaid by: {a}', file=sys.stderr)

    # create new quote and append to all_quotes
    all_quotes.append(Quote(t,a))

    #TODO add to quotes.txt

    #print(all_quotes.)
    return "return"



