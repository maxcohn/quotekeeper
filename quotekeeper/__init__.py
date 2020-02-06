import os
import sqlite3
from .routes import DATABASE_PATH
from flask import Flask, g

"""App factory function. Create the Flask application. When running the
application, Flask will automatically find this function and run it,
starting the application.
"""
def create_app():
    # create and configure the app
    app = Flask(__name__)

    # check if the 'quotes' table exists
    with sqlite3.connect(DATABASE_PATH) as conn:        
        # create database connection
        cursor = conn.cursor()
        cursor.execute("select count(*) from sqlite_master where type='table' and name='quotes'")
        if cursor.fetchone()[0] == 0:
            # table doesn't exist, so create one
            cursor.execute("create table quotes (quote text, author text)")
            conn.commit()

    # include blueprints
    from . import routes
    app.register_blueprint(routes.bp)

    # destroy database
    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    print("App beginning")
    return app


