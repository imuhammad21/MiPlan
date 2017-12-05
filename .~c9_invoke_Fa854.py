from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///miplan.db")
# db = SQL("postgres://plwpuvncsvzzvj:6d2bacc9737f579f4f0697b90361e375e1dc3d705522eaac3acdfd0b8ee50bf0@ec2-184-73-206-155.compute-1.amazonaws.com:5432/de2gv29arbdie5")
# def counter():

@app.route("/completed")
@login_required
def completed():
    taskid = request.values.get('done')
    db.execute("UPDATE tasks SET completed=:completed WHERE id=:taskid AND user_id=:id", completed="1",taskid=taskid, id=session["user_id"])
    return redirect("/")

@app.route("/delete")
@login_required
def delete():
    taskid = request.values.get('done')
    db.execute("DELETE FROM tasks WHERE id=:taskid AND user_id=:useid", taskid=taskid, id=session["user_id"])
    return redirect("/")

@app.route("/incomplete")
@login_required
def incomplete():
    psort = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0 ORDER BY priority", id=session["user_id"])
    db.execute("UPDATE tasks SET completed=:completed WHERE id=:taskid AND user_id=:id", completed="0",taskid=taskid, id=session["user_id"])
    return redirect("/")

@app.route("/psort")
@login_required
def psort():
    psort = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0 ORDER BY priority", id=session["user_id"])
    completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1", id=session["user_id"])
    return render_template("index.html",tasks=psort, completed=completed)


@app.route("/tsort")
@login_required
def tsort():
    tsort = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0 ORDER BY time", id=session["user_id"])
    completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1 ", id=session["user_id"])
    return render_template("index.html",tasks=tsort, completed=completed)

@app.route("/")
@login_required
def index():
    if request.method == "GET":
        tasks = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0", id=session["user_id"])
        completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1", id=session["user_id"])
        return render_template("index.html", tasks=tasks, completed=completed)
    if request.method == "POST":
        tasks = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0", id=session["user_id"])
        completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1", id=session["user_id"])
        return render_template("index.html",tasks=tasks, completed=completed)

@app.route("/home", methods = ["GET", "POST"])
def home():
        return render_template("home.html")

@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        # Ensure user inputs a task
        if not request.form.get("task"):
            message = "Please enter a task"
            return render_template("add.html", message=message)

        # Ensure user inputs a time
        if not request.form.get("time"):
            message = "Please enter a valid time"
            return render_template("add.html", message=message)

        # Add a new task into tasks database
        db.execute("INSERT INTO tasks(name, priority, time, user_id) VALUES(:name, :priority, :time, :id)",
                   name=request.form.get("task"), priority=request.form.get("priority"), time=request.form.get("time"),
                   id=session["user_id"])

        # Redirect to homepage
        return redirect("/")

    else:
        return render_template("add.html")


@app.route("/history")
@login_required
def tasks():
    tasks = db.execute("SELECT * FROM tasks WHERE user_id=:id", id=session["user_id"])
    return render_template("tasks.html", tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            message = "Please provide username"
            return render_template("login.html", message=message)

        # Ensure password was submitted
        elif not request.form.get("password"):
            message = "Please provide password"
            return render_template("login.html", message=message)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            message = "Invalid username and/or password"
            return render_template("login.html", message=message)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"]
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# @app.route("/quote", methods=["GET", "POST"])
# @login_required
# def quote():
#     if request.method == "POST":
#         # Ensure user inputs a symbol
#         if not request.form.get("symbol"):
#             return apology("Please enter a symbol")
#         # Ensure user inputs valid symbol
#         if not lookup(request.form.get("symbol")):
#             return apology("Please enter valid symbol")
#         info = lookup(request.form.get("symbol"))
#         # Redirect to a page that tells the user how much a share of the stock costs
#         return render_template("quoted.html", name=info["name"], price=info["price"], symbol=info["symbol"])
#     else:
#         return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks if user inputted username
        if not request.form.get("username"):
            message = "Missing username!"
            return render_template("register.html", message=message)
        # Checks if user inputted password
        if not request.form.get("password"):
            message = "Missing password!"
            return render_template("register.html", message=message)
        # Checks if password is 8 or more characters
        if len(request.form.get("password")) < 8:
            message = "Password must be at least 8 characters"
            return render_template("register.html", message=message)
        # Check if passwords match
        if request.form.get("password") != request.form.get("confirmation"):
            message = "Passwords do not match"
            return render_template("register.html", message=message)
        generate_password_hash(request.form.get("password"))
        # Record user into database
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"),
                            hash=generate_password_hash(request.form.get("password")))
        # Ensure username is not already being used
        if not result:
            message = "Username already in use"
            return render_template("register.html", message=message)
        session["user_id"] = result
        return redirect("/")

    else:
        return render_template("register.html")


# @app.route("/sell", methods=["GET", "POST"])
# @login_required
# def sell():
#     if request.method == "POST":
#         stock = lookup(request.form.get("symbol"))
#         # Ensure user inputted number of shares
#         if not request.form.get("shares"):
#             return apology("Enter a number of shares to sell")
#         # Ensure user inputted whole number for number of shares
#         if float(request.form.get("shares")) <= 0 or not request.form.get("shares").isdigit():
#             return apology("Ensure number of shares to sell is positive and a whole number")
#         # Declare table which has each symbol and total number of shares of that stock
#         shares = db.execute("SELECT SUM(number) FROM portfolio WHERE user_id=:id AND symbol=:symbol GROUP BY symbol",
#                             id=session["user_id"], symbol=request.form.get("symbol"))
#         # Set the sum of numbers equal to "number" in order to pass to sell.html
#         for i in range(len(shares)):
#             shares[0]["number"] = shares[i]["SUM(number)"]
#         # Ensure that user has enough shares to sell
#         if int(shares[0]["number"]) < int(request.form.get("shares")):
#             return apology("Don't have enough shares to sell")
#         # Add sale to cash
#         cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
#         db.execute("UPDATE users SET cash = :cash WHERE id=:id",
#                   cash=cash[0]["cash"] + stock["price"] * int(request.form.get("shares")), id=session["user_id"])
#         totalshares = shares[0]["number"] - int(request.form.get("shares"))
#         # Log sale into portfolio
#         db.execute("INSERT INTO portfolio(symbol, number, price, total, user_id) VALUES(:symbol, :number, :price, :total, :id)",
#                   symbol=request.form.get("symbol"), number=int(request.form.get("shares")) * -1, price=float(stock["price"]),
#                   total=stock["price"] * int(request.form.get("shares")), id=session["user_id"])
#         # Redirect to homepage
#         return redirect("/")
    # else:
    #     symbols = db.execute(
    #         "SELECT symbol FROM portfolio WHERE user_id=:id GROUP BY symbol", id=session["user_id"])
    #     return render_template("sell.html", symbols=symbols)



# def errorhandler(e):
#     """Handle error"""
#     return apology(e.name, e.code)


# # listen for errors
# for code in default_exceptions:
#     app.errorhandler(code)(errorhandler)
