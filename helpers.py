import csv
import urllib.request

from flask import redirect, render_template, request, session
from functools import wraps


def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # If user is not logged in, redirect to home page
        if session.get("user_id") is None:
            return redirect("/home")
        return f(*args, **kwargs)
    return decorated_function
