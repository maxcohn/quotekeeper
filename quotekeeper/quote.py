import os
import re
import sqlite3

# path to file in which quotes are stored
FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "quotes.db"))

# create database connection
conn = sqlite3.connect(FILE_PATH)
cursor = conn.cursor()

"""Reads in quote from quotes file given at FILE_PATH and returns a list of
Quote objects
"""
def read_quotes():
    # Read in everything from the database
    cursor.execute("select * from quotes")

    # list of Quote objects
    all_quotes = [Quote(t[0], t[1]) for t in cursor.fetchall()]

    return all_quotes


"""Class for containing quotes.
Stores text and author of quote
"""
class Quote:
    def __init__(self, t, a):
        self.text = t
        self.author = a

