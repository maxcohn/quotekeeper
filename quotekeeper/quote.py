import os
import re
import sqlite3

# path to file in which quotes are stored
FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "quotes.db"))

"""Reads in quote from quotes file given at FILE_PATH and returns a list of
Quote objects
"""
def read_quotes():
    with sqlite3.connect(FILE_PATH) as conn:        
        # create database connection
        cursor = conn.cursor()
        
        # check if the 'quotes' table exists
        cursor.execute("select count(*) from sqlite_master where type='table' and name='quotes'")
        if cursor.fetchone()[0] == 0:
            # table doesn't exist, so create one
            cursor.execute("create table quotes (quote text, author text)")
            cursor.commit()

        # Read in everything from the database
        cursor.execute("select * from quotes")

        # list of Quote objects
        all_quotes = [Quote(t[0], t[1]) for t in cursor.fetchall()]

        return all_quotes


def add_quote_db(t: str, a: str):
    with sqlite3.connect(FILE_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("insert into quotes (quote, author) values (?, ?)", (t, a))
        conn.commit()

"""Class for containing quotes.
Stores text and author of quote
"""
class Quote:
    def __init__(self, t, a):
        self.text = t
        self.author = a

