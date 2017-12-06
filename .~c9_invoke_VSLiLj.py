from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required

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


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///miplan.db")
# db = SQL("postgres://plwpuvncsvzzvj:6d2bacc9737f579f4f0697b90361e375e1dc3d705522eaac3acdfd0b8ee50bf0@ec2-184-73-206-155.compute-1.amazonaws.com:5432/de2gv29arbdie5")


@app.route("/completed")
@login_required
def completed():
    taskid = request.values.get('done')
    db.execute("UPDATE tasks SET completed=:completed WHERE id=:taskid AND user_id=:id", completed="1",taskid=taskid, id=session["user_id"])
    return redirect("/")

@app.route("/delete")
@login_required
def delete():
    taskid = request.values.get('delete')
    db.execute("DELETE FROM tasks WHERE id=:taskid AND user_id=:id", taskid=taskid, id=session["user_id"])
    return redirect("/")

@app.route("/incomplete")
@login_required
def incomplete():
    taskid = request.values.get('incomplete')
    db.execute("UPDATE tasks SET completed=:completed WHERE id=:taskid AND user_id=:id", completed="0",taskid=taskid, id=session["user_id"])
    return redirect("/")
sort = 1
@app.route("/psort")
@login_required
def psort():
    sort = 1
    psort = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0 ORDER BY priority", id=session["user_id"])
    completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1", id=session["user_id"])
    return render_template("index.html",tasks=psort, completed=completed)


@app.route("/tsort")
@login_required
def tsort():
    global sort = 2
    tsort = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0 ORDER BY time", id=session["user_id"])
    completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1 ", id=session["user_id"])
    return render_template("index.html",tasks=tsort, completed=completed)

@app.route("/")
@login_required
def index():
    if sort == 0:
        tasks = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0", id=session["user_id"])
        completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1", id=session["user_id"])
        return render_template("index.html", tasks=tasks, completed=completed)
    if sort == 1:
        psort = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0 ORDER BY priority", id=session["user_id"])
        completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1", id=session["user_id"])
        return render_template("index.html", tasks=psort, completed=completed)
    if sort == 2:
        tsort = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=0 ORDER BY time", id=session["user_id"])
        completed = db.execute("SELECT * FROM tasks WHERE user_id=:id AND completed=1", id=session["user_id"])
        return render_template("index.html", tasks=tsort, completed=completed)
@app.route("/home")
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

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return render_template("login.html", message="Please provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return render_template("login.html", message="Please provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return render_template("login.html", message="Invalid username and/or password")

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
    # Forget any user_id
    session.clear()
    # Redirect user to login form
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks if user inputted username
        if not request.form.get("username"):
            return render_template("register.html", message="Missing username!")
        # Checks if user inputted password
        if not request.form.get("password"):
            return render_template("register.html", message="Missing password!")
        # Checks if password is 8 or more characters
        if len(request.form.get("password")) < 8:
            return render_template("register.html", message="Password must be at least 8 characters")
        # Check if passwords match
        username = db.execute("SELECT username FROM users WHERE id=:id", id=result)
            return render_template("register.html", message="Passwords do not match")
        generate_password_hash(request.form.get("password"))
        # Record user into database
        result = db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get("username"),
                            hash=generate_password_hash(request.form.get("password")))
        # Ensure username is not already being used
        if not result:
            return render_template("register.html", message="Username already in use")
        session["user_id"] = result
        username = db.execute("SELECT username FROM users WHERE id=:id", id=result)
        session["username"] = username[0]['username']
        return redirect("/")
    else:
        return render_template("register.html")



