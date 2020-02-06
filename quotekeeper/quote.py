import os
import re
import sqlite3
from sqlite3 import Cursor


def all_quotes(cur: Cursor):
    """
    Reads in quote from quotes file given at FILE_PATH and returns a list of
    Quote objects
    """

    # Read in everything from the database
    cur.execute("select * from quotes")

    # list of Quote objects
    all_quotes = [Quote(t[0], t[1]) for t in cur.fetchall()]

    return all_quotes


def add_quote_db(cur: Cursor, t: str, a: str):
    """Adds a new quote to the database"""
    cur.execute("insert into quotes (quote, author) values (?, ?)", (t, a))

def filter_quote_name(cur: Cursor, name: str):
    """Filters quotes that contain `name` in the author section"""

        
    # Add wildcards for db pattern matching
    name = f"%{name}%"

    # Read in everything from the database
    cur.execute("select quote, author from quotes where author like ?", (name,))

    # list of Quote objects
    all_quotes = [Quote(t[0], t[1]) for t in cur.fetchall()]

    return all_quotes

def filter_quote_text(cur: Cursor, text: str):
    """Filters quotes that contain `text` in the quote section"""

    # Add wildcards for db pattern matching
    text = f"%{text}%"
    
    # Read in everything from the database
    cur.execute("select quote, author from quotes where quote like ?", (text,))

    # list of Quote objects
    all_quotes = [Quote(t[0], t[1]) for t in cur.fetchall()]

    return all_quotes



class Quote:
    """
    Class for containing quotes.

    Stores text and author of quote
    """
    def __init__(self, t, a):
        self.text = t
        self.author = a

