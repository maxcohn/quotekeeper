<<<<<<< Updated upstream
import os
import re

# path to file in which quotes are stored
FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "quotes.txt"))

"""Reads in quote from quotes file given at FILE_PATH and returns a list of
Quote objects
"""
def read_quotes():
    
    all_lines = None

    # read in all raw data
    with open(FILE_PATH, "r") as f:
        all_lines = f.readlines()
    
    # list of Quote objects
    all_quotes = []

    # regex to capture each side of '|'
    regex = re.compile(r'(.*)\|(.*)')

    # apply regex to all lines to get quotes and authors
    for i in all_lines:
        m = regex.match(i)

        # if line wasn't matched, just skip over it
        if m == None:
            continue

        q = m.group(1).strip()
        a = m.group(2).strip()
        all_quotes.append(Quote(q, a))

    return all_quotes


"""Class for containing quotes.
Stores text and author of quote
"""
class Quote:
    def __init__(self, t, a):
        self.text = t
        self.author = a
        
=======
import os
import re

# path to file in which quotes are stored
FILE_PATH = '/home/ubuntu/quotekeeper/quotes.txt'#os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "quotes.txt"))

"""Reads in quote from quotes file given at FILE_PATH and returns a list of
Quote objects
"""
def read_quotes():
    
    all_lines = None

    # read in all raw data
    with open(FILE_PATH, "r") as f:
        all_lines = f.readlines()
    
    # list of Quote objects
    all_quotes = []

    # regex to capture each side of '|'
    regex = re.compile(r'(.*)\|(.*)')

    # apply regex to all lines to get quotes and authors
    for i in all_lines:
        m = regex.match(i)

        # if line wasn't matched, just skip over it
        if m == None:
            continue

        q = m.group(1).strip()
        a = m.group(2).strip()
        all_quotes.append(Quote(q, a))

    return all_quotes


"""Class for containing quotes.
Stores text and author of quote
"""
class Quote:
    def __init__(self, t, a):
        self.text = t
        self.author = a
        
>>>>>>> Stashed changes
