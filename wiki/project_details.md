# Team TBD Project Details

## A Calendar-based Productivity Application

### What is your project all about? What are you trying to achieve?

Our team recognizes that graduate students can have a hard time managing responsibilities, deadlines, and other commitments. As a result, our team decided that we would develop a calendar web application. Our web app will allow users to create and manage an account, view all upcoming tasks and reminders, and create new calendar reminders. In addition, users will be able to track the number of hours they have spent on specific tasks. If time permits, we would also like to set up a service that will send an email to the user about upcoming reminders.

### What technologies are you using?

Our web app will consist of a Python client-side app, a Flask server, and a SQLite database. In addition, we are going to be implementing a form of monitoring for the entire system, although the logistics of this have not been fully discussed.

### How are you deploying your system?

It will be deployed on Heroku and can be found here: [Staging](https://team-tbd-project-staging.herokuapp.com), [Production](https://team-tbd-project-production.herokuapp.com).

### What design decisions have you made?

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

Our UI design can be found [here](https://github.com/CSCI-5828-Foundations-Sftware-Engr/team-tbd-semester-project/blob/main/wiki/wireframe.md).

Our database currently consists of a user table to store basic user info, a reminder table that stores all reminders for all users (it is indexed on userid), and two look up tables. The database diagram can be seen below.

![Database diagram](https://user-images.githubusercontent.com/43146669/228691580-487dc0d8-325a-4c1d-85c6-46bd41aae404.png)

Below is a diagram of a basic sequence where the user logs in, sees all saved reminders, and adds a new reminder.

![Calendar Sequence](https://user-images.githubusercontent.com/43146669/227093778-ec07dcbc-7d5e-40a3-be70-7f0eff0f048b.jpg)

We have also created the basic layout of our UI. 
