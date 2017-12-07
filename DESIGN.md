From a visual standpoint our project may look simple (that was one of the design goals), but from a technical standpoint, there are many
creative elements implemented within the neat framework. The first page the user is taken to when typing in the website is the home page,
with two large buttons allowing users to register or login.  We decided to have a homepage that gave both options as opposed to a login
page that supplied the option to register because we felt that it simplifies the process for new users while also taking advantage of
white space in an aesthetically-pleasing way.  We felt that it made more sense to have an interface that new users would be just as
comfortable navigating as returning ones so that their first interaction with the website is an inviting and intuitive one.

Should the user click the button to register, they will be taken to a page that has a form requesting username, a password longer than
eight characters, and a password confirmation.  We placed this form in the center of the page both vertically and horizontally to
subconsciously remind the user that when they are on the register page, this form is the only thing to which they should be paying
attention.  Should the user fail to provide a username or password, an alert will pop up on the same page saying "Please enter a
username/password", and then the register page reloads, allowing the user to submit the form again.  In addition, should a username
already be in use, an alert pops up that says "Username already in use".  Finally, if the user submits two passwords that don't match,
or a password shorter than eight characters, a message will pop up that tells them what they need to fix and reloads the page.  If the
user registers correctly, their user id, username, and hash of their password will be stored in the users database to keep track of
their tasks.

The popup alert messages are called by returning a value "message" to each html page using render_template.  The html pages have a
if condition that says if a message is returned, display this message as a popup, and then proceeds to relaod the page once "OK" is
pressed by the user.

Should the user click the button to login, they will be taken to a page that has a form requesting a username and password.  Similar
to register, should the user not enter a username or password, an alert will pop-up telling them to do so and the page will be reloaded
allowing them to submit the form again.  If the user inputs an invalid username or password, and alert will also pop-up notifying
the user which one is incorrect and reload the page.  If the user logs in correctly, they will have access to the tasks that are associated
with their unique user id stored in both the users and tasks databases

Once the user registers or logs in, they will be taken to an index page, which is where they can view their tasks.  Upon first
registering, the user will not have any tasks in their "active task" table or their "completed" table, so they will likely want to
click the "Add Task" button in the navigation bar in order to add a new task. Should the user click the "Add Task" button, they will
be taken to a page that has a form requesting a task name, 1 of 4 priority levels ranging from low to critical, and a due date and
time when the task needs to be complete.

Once the user has inputted a couple of tasks, the app becomes much more useful.  For one, a user can not only view the date when a
task is due, but also a countdown timer that displayes how much real time the user has to complete it.  We decided to include the timer
because we felt that something ticking off every second would add an extra incentive to use one's time quickly and effectively, rather
than just seeing a static date that may not mean much in someone's busy life.  In addition, viewing a timer as opposed to the date a
task is due eliminates the need for the user to determine which task is most pressing from a time perspective; the app does it for them.
For a similar reason, we display the user-inputted priority associated with each task in the table to incentivize the user to complete
the tasks that not only are the most time-pressing, but are the most important.  This feature helps to prevent a user from seeing
that they may have ample time to complete a few tasks and become complacent, because it demonstrates that some or more important than
others and creates the incentive to get a head start on those tasks that may be of a "high" or "critical" priority.  All of these
qualities are features of the "Active Tasks" Table, which is used for tasks that have not yet been completed.

The whole point of a task manager is to complete the tasks that are on your plate, so in the "Active Tasks" table, we have added a
"done" button associated with each task on the far right in order to have a tangible representation on the app of completing something.
Each task in the "tasks" table has an element called "completed" which by default has a value of zero.  Once a user clicks the "done"
button, they call the "completed" function that changes the value of "completed" for that particular tasks to 1 and returns the user
back to the index page with the updated database.  Index selects those values in the tasks table (for a particular user) with values
of completed = 0 and puts them in the "Active Tasks" table and those with values of completed = 1 and puts them in the "Completed Tasks"
table.  Therefore, the "done" button essentially moves a tasks from the "Active Tasks" table to the "Completed Tasks" table. In this
"Completed Tasks" table, the user no longer sees the "time remaining" to complete the task, because it is already complete.  Instead,
the user can view the task name, due date, a button to return the task to the "active tasks" table, and a button to delete the task.
One of the greatest feelings after a long day of work is to see how much was actually completed, which is the point of the "Completed
Tasks" table.  In addition, viewing a task move from the active table to the completed table instead of simply disappearing visually
reinforces the notion that work was put in to complete the task.  However, after one's task list becomes long, it may become cumbersome
to have tasks from a month ago still visible on one's interface.  We solved this problem by adding a delete button that deletes the
entry of a particular tasks from the database and therefore is gone from the "Completed Tasks" table once the page is reloaded.

In addition to being able to add, complete, and delete tasks, we offer the user the ability to sort the order in which each task
is shown to them in the "Active Tasks" page by priority and time.  The titles of the columns for Priority and Due Date are actually
buttons to sort the tasks by their respective attributes.  We define a global variable "sort" at the beginning of our application and
set it to default, which will show the task that was inputted the most recently at the top of the list.  When the user clicks the button
"priority", they are also calling the function "psort", which sets the global sort variable eaual to "priority".  The user is then
redirected to the index page, but the index function has an if statement that selects data in a particular order based off of the sort
variable.  If sort equals "priority", then index selects the data from the tasks database ordered by priority and displays it with the
most pressing tasks first. In the same way, clicking the "due date" button sets the global sort variable to "time" and tells index
to select the data from the tasks database ordered by time and displays it with the most time sensitive tasks first.

Once logged in, the navigation bar contains buttons that give the user the option to add a new task, return to the index page(via the
'tasks' button), and logout.  If the user is logged out, the navigation bar simply says "MiPlan" in the top left and the user is given
the option to login and to register.