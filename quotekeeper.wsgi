

import logging
import sys
logging.basicConfig(stream=sys.stderr)

# change this to the correct directory
sys.path.insert(0, '/var/www/html/quotekeeper')

import quotekeeper
application = quotekeeper.create_app()
