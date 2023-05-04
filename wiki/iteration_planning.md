# Team TBD - Iteration Planning

## Sprint 1 - Login Page + Calendar + Database - 4/3-4/10

![Burndown](https://user-images.githubusercontent.com/43146669/230262161-991c278f-cf9a-4336-ae3c-403c84a89c43.png)

* Created a basic UI for a calendar with events populated from an example .JSON file.
* Set up a SQLite database with corresponding tables for users and calendar events. 
* Basic Flask server created with API routes for monitoring and testing basic GET/POST requests for logging in.

## Sprint 2 - More Calendar Features + Authorization + Reminders - 4/10-4/20

![Burndown 2](https://user-images.githubusercontent.com/43146669/233540053-cfd433d5-3c08-4358-be69-ef0ea2d0216b.png)

* Integration of authorization with calendar UI.
* Basic reminders API completed so events can be added and deleted from the database.
* Database expanded to account for recurring events and other more narrow functionalities.

# PRESENTATION ON 4/20

## Sprint 3 - Calendar Integrations + Data Collector + Data Analyzert - 4/20-4/27
![burndown 3](https://user-images.githubusercontent.com/43146669/236079006-64f34ed4-bbaf-4f73-ac19-2f9b7d805e44.png)

* Integration of the calendar frontend with the backend.
* Add and delete functionalities added to the calendar.
* Data Collector set up completed to retrieve match data from the API and stored in a database.
* Created a data analyzer to filter out matches from the list of events if they conflict with any of the user's reminders.

## Sprint 4 - Deployment + CI/CD + Monitoring +Integration Tests 4/27-5/3
![burndown 4](https://user-images.githubusercontent.com/43146669/236081327-acc30e59-710d-49c4-b3d3-7901ae2ce7ff.png)

* Github Actions set up for CI.
* Caching error resolved.
* Integration testing performed using Selenium to ensure that all functionalities are performing as expected after the integration.
