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

1. Navigate into a directory with the `quotekeeper` package.

2. In that directory, there should be a file called `quotes.txt`. This stores
the quotes with a simple format. More about the format [here](#quote-format)

3. Run the Flask app with `FLASK_APP=quotekeeper` as an environment variable.

4. You should be good!

## Routes:
* '/newquote' [POST] - Route to post new quotes to to be added to the database (or json???)

* '/' [GET] - Home page that display quotes, also has option to add quotes

## Quote Format

I considered using a database for this, but I figured that there isn't much
of a reason considering there are no lookups, just displaying of all content.
Adding a database seemed like it would only cause extra complication for
a project as small as this.

Performance shouldn't be much of a concern considering the quotes are only
ever read from the file on startup.

The format looks like this:
```
the actual quote|the author/context of the quote
```

White space between the pipe and either side doesn't matter.

## What did I learn from this project?

I had never really used Flask for anything more than one file projects, so
this was a nice introduction to the idea of that.

In general, I don't have much experience with backend development. I figure
that it'll be a great set of skills to have.

I have just recently come around to Python, so I wasn't very familiar with
the way Python handles modules and packages. This project led me to learning
what those words mean to Python and how to use each of them, which will
definitely come in handy.

## Potential changes

I may add a password for sending quotes just because I know the ability to
add quote form anywhere will be abused by my friends.


# TODO

Nothing right now