# Team TBD Project Details

## A Calendar-based Productivity Application

### What is your project all about? What are you trying to achieve?

Our team recognizes that graduate students can have a hard time managing responsibilities, deadlines, and other commitments. As a result, our team decided that we would develop a calendar web application. Our web app will allow users to create and manage an account, view all upcoming tasks and reminders, and create new calendar reminders. In addition, users will be able to track the number of hours they have spent on specific tasks. If time permits, we would also like to set up a service that will send an email to the user about upcoming reminders.

### What technologies are you using?

Our web app will consist of a Python client-side app, a Flask server, and a SQLite database. In addition, we are going to be implementing a form of monitoring for the entire system, although the logistics of this have not been fully discussed.

### How are you deploying your system?

It will be deployed on Heroku and can be found here: [Staging](https://team-tbd-project-staging.herokuapp.com), [Production](https://team-tbd-project-production.herokuapp.com).

### What design decisions have you made?

Our UI design can be found [here](https://github.com/CSCI-5828-Foundations-Sftware-Engr/team-tbd-semester-project/blob/main/wiki/wireframe.md).

Our database currently consists of a user table to store basic user info, a reminder table that stores all reminders for all users (it is indexed on userid), and two look up tables. The database diagram can be seen below. We chose to use SQLite for this database because it is lightweight. The basic features it offers are sufficient for our project and allow us to easily store and access data without much overhead.

![Database diagram](https://user-images.githubusercontent.com/43146669/228691580-487dc0d8-325a-4c1d-85c6-46bd41aae404.png)

Below is a diagram of a basic sequence where the user logs in, sees all saved reminders, and adds a new reminder.

![Calendar Sequence](https://user-images.githubusercontent.com/43146669/227093778-ec07dcbc-7d5e-40a3-be70-7f0eff0f048b.jpg)

We have also created the basic layout of our UI. 

### What processes are you using to coordinate your team?

We are co-ordinating the team using [Trello](https://trello.com/invite/b/qDzf7Ekl/ATTI9736135482b19ca5c804278553f2fbf6DFCBF349/team-tbd). This allows us to keep all of our user stories in what place, and is an accessible way to manage sprints, as well as view our burndown chart. Communication is orchestrated over a Slack channel, and we use GitHub for source control of all the code relevant to our project.

### How is work distributed across the team? Who is doing what for each iteration?

We have roughly divided the work among the 4 members in the following way:
| Member  | Responsibilities |
| ------------- | ------------- |
| Sukeerth Kalluraya | Frontend, Authentication  |
| Scott McCall  | Flask Server + API  |
| Paresha Farastu  | UX, Frontend  |
| Thomas Starnes  | Datbase, API, Authentication  |

## Unit Testing

For our application, our team has created two sets of unit tests, one to test the authorization components of the API (auth_test.py), and one to test the reminders (reminders_test.py). All testing is done using a Python module called unittest. For the authorization, there are a total of 6 unit tests that comprehensively test the expected behaviors of our system. The first test makes sure that the server is running. The second test makes attempts to make a request to a protected webpage that requires authorization. The test expects a 401 response code because no authorization has been provided. The third test verifies login functionality using a default email and password that is included in the database. The fourth test then tries to access the same protected API route, and this time expects a success now that the user has logged in. The fifth test verifies the logout functionality, and the sixth test confirms that the user has lost authorization after logging out by trying to access the protected route again.

For our reminders test, we have created three different tests, one for retrieving the reminders of a given user, one for adding an event to the database, and one for deleting an event from the database.

As of the end of our Homework 7 iteration on 4/20, all 6 of our authorization tests are passing and all 3 of our reminders tests are passing.
