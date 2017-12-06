# MiPlan
    Our project, MiPlan, is an extremely user friendly web based application that allows users to manage their tasks. The home page greets
the user with two choices, login or register. New users will need to regiser while existing users can simply login with their username and
password as they would on any other web based application. When registering the user will be prompted for a username, a password that is
greater than 8 characters, and a confirmation of the password. If any of these are not filled out, the username is already taken, the
password isn't long enough, or the passwords don't match, an error alert in the form of a popup will notify the user of their specific
mistake. Once successfully registered, the user can then log in to the application using the login choice on the homepage which works
just like any other web based application, prompting the user for a username and password. If the user makes an error on the login,
they will be notified with a popup alert that either their username or password is invalid.
    Once the user succesfully completes the registration or logs in, the user will be taken to the tasks page where they will find two
tables, one labeled Active Tasks, and the other, Completed Tasks. To add a task, the user clicks on the blue button in the navigation bar
that says "Add Task". This brings them to a new window where they must input a description of the task itself, choose its priority from a
drop down menu that includes "Low", "Intermediate", "High", and "Critical", and also enter the task's due time and date. As default,
the priority default is set at low, but if either the task text box or the date-time form are left blank, the user will receive
a respective error message telling them of their mistake. Once a user has filled out all the forms, they click the "Add Task" button
and the task gets added into the "Active Tasks" table.
    In the "Active Tasks" table, the user is shown the task itself, its priority, its due date, a countdown counter that displays the
time remaining until the due date, and the option to mark the task as complete with a "Done" button. Additionally, the "Priority" and
"Due Date" columns are buttons which can be clicked to sort the tasks by priority from "Critical" to "Low", or sort by Due Date from the
most time sensitive to the least. If the "Done" button is clicked in the "Click to Complete" column of "Active Tasks", the task moves to
the "Completed Tasks" table. In this table, the task can be returned to the "Active Tasks" table with the "Incomplete" button in the
"Return to Active" column, or it can be deleted forever with "Delete" button.
    In the navigation bar, there are three buttons which can be accessed at any time when the user is logged in. They are "Add Task",
"Tasks", and "Logout". Additionally in the navigation bar, the user who is currently logged in is displayed so that the user knows
that the tasks are in fact theirs. The buttons are all self explanatory, "Add Task" brings you to the page where you can add a task,
"Tasks" brings you to the page where all your Active and Completed tasks are displayed, and "Log Out", logs out the current user and
redirects them to the homepage (with the "Login" and "Register" buttons).
    At the moment, MiPlan lives only within the CS50 IDE and can be activated with flask run.