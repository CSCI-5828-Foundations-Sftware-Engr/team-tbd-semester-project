# Team TBD Semester Project
## A Calendar-based Productivity Application

Our team recognizes that graduate students can have a hard time managing responsibilities, deadlines, and other commitments. As a result, our team decided that we would develop a calendar web application. Our web app will allow users to create and manage an account, view all upcoming tasks and reminders, and create new calendar reminders. If time permits, we want.  We would aslo like to set up a service that will send an email to the user about an upcoming reminder.

Our web app will consist of a Python client-side app, a Flask server, and a SQLite database. It will be deployed on Heroku and can be found here: [Staging](https://team-tbd-project-staging.herokuapp.com), [Production](https://team-tbd-project-production.herokuapp.com).

Our database currently consists of a user table to store basic user info, a reminder table that stores all reminders for all users (it is indexed on userid), and two look up tables. The database diagram can be seen below.

![Database diagram](https://user-images.githubusercontent.com/43146669/228691580-487dc0d8-325a-4c1d-85c6-46bd41aae404.png)

Below is a diagram of a basic sequence where the user logs in, sees all saved reminders, and adds a new reminder.

![Calendar Sequence](https://user-images.githubusercontent.com/43146669/227093778-ec07dcbc-7d5e-40a3-be70-7f0eff0f048b.jpg)

