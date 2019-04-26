import os

from flask import Flask

"""App factory function. Create the Flask application. When running the
application, Flask will automatically find this function and run it,
starting the application.
"""
def create_app():
    # create and configure the app
    app = Flask(__name__)

    # include blueprints
    from . import routes
    app.register_blueprint(routes.bp)

    return app


"""
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "fuck"
    #return render_template("%s.html" % "index")

@app.route('/new', methods=['POST'])
def new_quote():
    print(request.get_json())
"""