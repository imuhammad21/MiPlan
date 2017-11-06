from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

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
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    portfolio_stock = db.execute(
        "SELECT number, symbol, id FROM portfolio WHERE user_id =:id", id=session["user_id"])

    totalcash = 0
    for stock in portfolio_stock:
        symbol = stock["symbol"]
        number = stock["number"]
        id = stock["id"]
        if not lookup(symbol):
            return apology("Try Again")
        current_price = lookup(symbol)["price"]
        total = number * current_price
        totalcash += total
        db.execute("UPDATE portfolio SET price =:price, total =:total WHERE user_id=:user_id AND symbol=:symbol AND id=:id",
                   price=current_price, total=total, user_id=session["user_id"], symbol=symbol, id=id)
    cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
    totalcash += cash[0]["cash"]
    uportfolio = db.execute(
        "SELECT symbol, price, SUM(number), SUM(total), user_id FROM portfolio WHERE user_id=:id GROUP BY symbol", id=session["user_id"])
    for i in range(len(uportfolio)):
        uportfolio[i]["number"] = uportfolio[i]["SUM(number)"]
        uportfolio[i]["total"] = uportfolio[i]["SUM(total)"]

    return render_template("index.html", uportfolio=uportfolio, cash=usd(cash[0]["cash"]), total=usd(totalcash))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("Please enter a symbol")

        if not lookup(request.form.get("symbol")):
            return apology("Please enter valid stock")

        if not request.form.get("shares"):
            return apology("Enter a number of shares to buy")
        stock = lookup(request.form.get("symbol"))
        try:
            int(request.form.get("shares"))
        except:
            return apology("Enter whole number of shares to buy")
        if float(request.form.get("shares")) <= 0 or not request.form.get("shares").isdigit():
            return apology("Enter whole number of shares to buy")
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])

        if float(stock["price"]) * int(request.form.get("shares")) > cash[0]["cash"]:
            return apology("Cannot Afford")

        db.execute("UPDATE users SET cash = :cash WHERE id=:id", cash=cash[0]["cash"] - stock["price"] * int(request.form.get("shares")),
                   id=session["user_id"])
        number = db.execute("SELECT number FROM portfolio WHERE user_id=:id AND symbol=:symbol",
                            id=session["user_id"], symbol=request.form.get("symbol"))

        db.execute("INSERT INTO portfolio(symbol, number, price, total, user_id) VALUES(:symbol, :number, :price, :total, :id)",
                   symbol=request.form.get("symbol"), number=int(request.form.get("shares")), price=float(stock["price"]),
                   total=stock["price"] * int(request.form.get("shares")), id=session["user_id"])

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    transactions = db.execute("SELECT * FROM portfolio WHERE user_id=:id", id=session["user_id"])
    return render_template("history.html", transactions = transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        # Ensure user inputs a symbol
        if not request.form.get("symbol"):
            return apology("Please enter a symbol")
        # Ensure user inputs valid symbol
        if not lookup(request.form.get("symbol")):
            return apology("Please enter valid symbol")
        info = lookup(request.form.get("symbol"))
        # Redirect to a page that tells the user how much a share of the stock costs
        return render_template("quoted.html", name=info["name"], price=info["price"], symbol=info["symbol"])
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks if user inputted username
        if not request.form.get("username"):
            return apology("Missing username!")

        # Checks if user inputted password
        if not request.form.get("password"):
            return apology("Missing password!")
        # Checks if password is 9 or more characters
        # if len(request.form.get("password")) <= 8:
            # return apology("Password must be 8 characters")
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match")
        generate_password_hash(request.form.get("password"))
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"),
                            hash=generate_password_hash(request.form.get("password")))
        if not result:
            return apology("Username already in use")
        session["user_id"] = result
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "POST":
        stock = lookup(request.form.get("symbol"))
        # Ensure user inputted number of shares
        if not request.form.get("shares"):
            return apology("Enter a number of shares to sell")
        # Ensure user inputted whole number for number of shares
        if float(request.form.get("shares")) <= 0 or not request.form.get("shares").isdigit():
            return apology("Ensure number of shares to sell is positive and a whole number")
        # Declare table which has each symbol and total number of shares of that stock
        shares = db.execute("SELECT SUM(number) FROM portfolio WHERE user_id=:id AND symbol=:symbol GROUP BY symbol",
                            id=session["user_id"], symbol=request.form.get("symbol"))
        for i in range(len(shares)):
            shares[0]["number"] = shares[i]["SUM(number)"]
        if int(shares[0]["number"]) < int(request.form.get("shares")):
            return apology("Too Many Shares")
        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        db.execute("UPDATE users SET cash = :cash WHERE id=:id",
                   cash=cash[0]["cash"] + stock["price"] * int(request.form.get("shares")), id=session["user_id"])
        totalshares = shares[0]["number"] - int(request.form.get("shares"))

        cash = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        if float(stock["price"]) * int(request.form.get("shares")) > cash[0]["cash"]:
            return apology("Cannot Afford")
        db.execute("INSERT INTO portfolio(symbol, number, price, total, user_id) VALUES(:symbol, :number, :price, :total, :id)",
                   symbol=request.form.get("symbol"), number=int(request.form.get("shares")) * -1, price=float(stock["price"]),
                   total=stock["price"] * int(request.form.get("shares")), id=session["user_id"])
        return redirect("/")
    else:
        symbols = db.execute(
            "SELECT symbol FROM portfolio WHERE user_id=:id GROUP BY symbol", id=session["user_id"])
        return render_template("sell.html", symbols=symbols)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
