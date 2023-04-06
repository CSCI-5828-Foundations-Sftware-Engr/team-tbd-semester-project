# Team TBD Project Details

## A Calendar-based Productivity Application

Our team recognizes that graduate students can have a hard time managing responsibilities, deadlines, and other commitments. As a result, our team decided that we would develop a calendar web application. Our web app will allow users to create and manage an account, view all upcoming tasks and reminders, and create new calendar reminders. If time permits, we want.  We would aslo like to set up a service that will send an email to the user about an upcoming reminder.

Our web app will consist of a Python client-side app, a Flask server, and a SQLite database. It will be deployed on Heroku and can be found here: [Staging](https://team-tbd-project-staging.herokuapp.com), [Production](https://team-tbd-project-production.herokuapp.com).

We are co-ordinating the team using [Trello](https://trello.com/invite/b/qDzf7Ekl/ATTI9736135482b19ca5c804278553f2fbf6DFCBF349/team-tbd).

We have roughly divided the work among the 4 members in the following way:
| Member  | Responsibilities |
| ------------- | ------------- |
| Sukeerth Kalluraya | Frontend, Authentication  |
| Scott McCall  | Flask Server + API  |
| Paresha Farastu  | UX, Frontend  |
| Thomas Starnes  | Datbase, API, Authentication  |

Our database currently consists of a user table to store basic user info, a reminder table that stores all reminders for all users (it is indexed on userid), and two look up tables. The database diagram can be seen below.

![Database diagram](https://user-images.githubusercontent.com/43146669/228691580-487dc0d8-325a-4c1d-85c6-46bd41aae404.png)

Below is a diagram of a basic sequence where the user logs in, sees all saved reminders, and adds a new reminder.

![Calendar Sequence](https://user-images.githubusercontent.com/43146669/227093778-ec07dcbc-7d5e-40a3-be70-7f0eff0f048b.jpg)

We have also created the basic layout of our UI. 

### UI Design
![log in](https://user-images.githubusercontent.com/43146669/230254393-69cc5ac1-63be-4bd9-b52b-0952913bf2f4.png)
![monthly](https://user-images.githubusercontent.com/43146669/230254392-eb71eff3-2192-42aa-9968-345300db5b3e.png)
![weekly](https://user-images.githubusercontent.com/43146669/230254391-8a8ff689-37ee-4a00-85be-81958bb363a5.png)
![daily](https://user-images.githubusercontent.com/43146669/230254390-7fac5486-a29c-4457-9025-e80c8b5e9ef0.png)
