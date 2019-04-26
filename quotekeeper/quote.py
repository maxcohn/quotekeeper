import os
import re

class Quote:
    def __init__(self, t, a):
        self.text = t
        self.author = a
    
    @staticmethod
    def get_quotes():
        # get path so we can open the file containing quotes
        basepath = os.path.dirname(__file__)
        filepath = os.path.abspath(os.path.join(basepath, "..", "quotes.txt"))
        
        all_lines = None

        # read in all raw data
        with open(filepath, "r") as f:
            all_lines = f.readlines()
        
        # list of Quote named tuples
        all_quotes = []

        # regex to capture each side of '|'
        regex = re.compile(r'(.*)\|(.*)')

        # apply regex to all lines to get quotes and authors
        for i in all_lines:
            m = regex.match(i)
            q = m.group(1).strip()
            a = m.group(2).strip()
            all_quotes.append(Quote(q, a))

        return all_quotes
