# Quote Keeper

Flask server that allows for the storage of quotes

This is my first attempt at a Flask application that is larger than a single file.

## Why?

My friends and I have had a quote board that we fill with our absurd sayings
for quite some time, but we would often forget to add quotes that were said
outside of the apartment/dorm, or sometimes we just wanted to get the
exact wording on that insane thing that Liam said. This seemed like a quick
way to solve those problems.

## How to run

1. Run the Flask app as you usually would

2. A new file will be created in the root directory of the project (`quotes.db`)

3. This file is the SQLite database that the app uses to keep track of quotes

4. There is no special setup for the database, the app should handle everything.

## Routes:
* '/newquote' [POST] - Route to post new quotes to to be added to the database

* '/' [GET] - Home page that display quotes

* '/submitquote' [GET] - Page that has form to submit quotes

* '/filter/name/<name\>' [GET] - Same as home page, but filters for quotes that
contain `name` in the author section

* '/filter/text/<text\>' [GET] - Same as homepage, but filters for quotes that
contain `text` in the text section

## Quote storage

I chose to store the quotes in a SQLite database for a few reasons. They're
fast, efficient, and easy in Python.

## What did I learn from this project?

I had never really used Flask for anything more than one file projects, so
this was a nice introduction to the idea of that.

In general, I don't have much experience with backend development. I figure
that it'll be a great set of skills to have.

I have just recently come around to Python, so I wasn't very familiar with
the way Python handles modules and packages. This project led me to learning
what those words mean to Python and how to use each of them, which will
definitely come in handy.

## Files explained

* `quote.py` - Quote object and helper functions for reading and writing quotes

* `routes.py` - Routes and code associated with handling all route in the app

* `__init__.py` - Handles WSGI app creation

* `static/` - Directory for static content

* `templates/` - Directory of Jinja templates

#### Why is there a separate page to submit quotes?

I did this as a rudimentary way of making quote submission exclusive to those
who are participants in the website. This way when someone stumbles upon it,
there is no greifing that can be done from the homepage.

## TODO

* Clean up everything. This was made when I was new to web frameworks and databases,
so this needs a good refactoring

* Figure out how to design search so that it has the option to search by text