# [UnicornAttractor](https://unicorn-attractor-ms4-hebs87.herokuapp.com/) - Milestone Project Four

[![Build Status](https://travis-ci.org/hebs87/unicorn-attractor-milestone-four.svg?branch=master)](https://travis-ci.org/hebs87/unicorn-attractor-milestone-four)

## Table of Contents

- [**About**](#About)
  - [Why This Project?](#Why-This-Project)
- [**UX**](#UX)
  - [User Stories](#User-Stories)
  - [Style Rationale](#Style-Rationale)
  - [Wireframes](#Wireframes)
  - [Database Schema](#Database-Schema)
- [**Features**](#Features)
  - [Functionality](#Functionality)
  - [Existing Features](#Existing-Features)
  - [Features Left To Implement](#Features-Left-To-Implement)
- [**Technologies Used**](#Technologies-Used)
  - [Version Control](#Version-Control)
  - [Hosting](#Hosting)
- [**Testing**](#Testing)
  - [Testing User Stories](#Testing-User-Stories)
  - [Responsive and Functional Testing](#Responsive-and-Functional-Testing)
  - [Additional Testing](#Additional-Testing)
  - [Code Validation](#Code-Validation)
  - [Automated Testing](#Automated-Testing)
  - [Travis Continuous Integration](#Travis-Continuous-Integration)
  - [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
  - [Media And Static Folders](#Media-And-Static-Folders)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

This application (app) is an issue tracker for a game called UnicornAttractor. UnicornAttractor isn't a real game, but the site allows users to log Bug Reports or Feature Requests relating to the make-believe game, and they can also upvote, downvote and comment on existing tickets by creating their own account and profile.

### Why This Project?

I created this app for the Full Stack Frameworks project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to create an issue tracking web application, which allows users to submit bug tickets for free, or requests for additional features for a small fee. Users should also have the ability to upvote and comment on tickets, to guide prioritisation.

The front-end display and functionality uses HTML, CSS and JavaScript. The back-end functionality uses Python, Django, SQLite3 and PostgreSQL.

## UX

### User Stories

As a user, I want to be able to:
- View all bug and feature tickets logged by other users, as a guest - Done
- Register for my own account - Done
- Reset my account password if I forget it - Done
- Log bug tickets for free - Done
- Log feature request tickets by paying a small fee - Done
- Edit bug and feature tickets that I’ve created - Done
- Delete bug and feature tickets that I’ve created - Done
- Filter and search for tickets using various categories - Partially done (search functionality not built)
- Comment on any tickets that have been logged by me or other users - Done
- Upvote existing bug tickets for free - Done
- Upvote existing feature tickets by paying a small fee - Done
- View a dashboard containing various ticket statistics - Done

### Style Rationale

The style and colour scheme used in my app was inspired by the picture that I used for the logo. I wanted the site to be bright and have a 'magical' feel to it, given that Unicorns are mythical creatures.

### Wireframes

I drew my wireframes using Balsamiq. I have done separate wireframes to show my consideration of how to make my website/app responsive. The links to the files are below:

- [Home - no user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/home-xs-sm-md-no-user-login.png)
- [Home - no user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/home-xl-lg-no-user-login.png)
- [Home - user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/home-xs-xm-md-user-logged-in.png)
- [Home - user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/home-xl-lg-user-logged-in.png)
- [Log In (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/log-in-xs-sm-md.png)
- [Log In (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/log-in-lg-xl.png)
- [Register (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/register-xs-sm-md.png)
- [Register (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/register-lg-xl.png)
- [Profile (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/profile-xs-sm-md.png)
- [Profile (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/profile-lg-xl.png)
- [Statistics (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/statistics-xs-sm-md.png)
- [Statistics (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/statistics-lg-xl.png)
- [Tickets - no user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/tickets-xs-sm-md-no-user-login.png)
- [Tickets - no user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/tickets-lg-xl-no-user-login.png)
- [Tickets - user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/tickets-xs-sm-md-user-logged-in.png)
- [Tickets - user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/tickets-lg-xl-user-logged-in.png)
- [Log A Bug (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/log-a-bug-xs-sm-md.png)
- [Log A Bug (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/log-a-bug-lg-xl.png)
- [Log A Feature (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/log-a-feature-xs-sm-md.png)
- [Log A Feature (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/log-a-feature-lg-xl.png)
- [Bug - no user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/bug-xs-sm-md-no-user-login.png)
- [Bug - no user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/bug-lg-xl-no-user-login.png)
- [Bug - user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/bug-xs-sm-md-user-logged-in.png)
- [Bug - user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/bug-lg-xl-user-logged-in.png)
- [Feature - no user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/feature-xs-sm-md-no-user-login.png)
- [Feature - no user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/feature-lg-xl-no-user-login.png)
- [Feature - user logged in (xs, sm and md)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/feature-xs-sm-md-user-logged-in.png)
- [Feature - user logged in (lg and xl)](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/wireframes/feature-lg-xl-user-logged-in.png)

There are some differences between my wireframes and my final website. This was due to visual preferences and feedback received from my mentor, and also other users who tested my website.

### Database Schema

Before building my project, I created an Entity Relationship (ER) diagram to outline the database schema for the various tables that I would use. The link to the file is below:

- [UnicornAttractor Database Schema](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/schema/unicorn-attractor-db-schema.pdf)

## Features

### Functionality

The app uses Python logic to allow users to login or register for a free account. The app offers CRUD operations to allow users to create, read, update and delete tickets. Users can filter tickets based on various categories. Additionally, users can upvote or downvote tickets - upvoting feature tickets requires a small donation.

I added some additional features that weren't within the scope of the project, as I felt that they offered better interactivity for users.

### Existing Features

- **Navbar/Sidenav Links** - The navbar and sidnav links vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Home', 'Tickets', 'Login' and 'Register' links are shown. When the user is logged in, the 'Home', 'Tickets', 'Profile' and 'Logout' links are shown.
- **App Store/Google Play Buttons** - The App Store button loads the Apple App store in a new browser tab. The Google Play button loads the Google Play store in a new browser tab. While the UnicornAttractor app isn't actually a real app available for download, this creates authenticity for the user by giving them the impression that they can download it.
- **Index Links/Buttons** - The links and buttons on the index page vary depending on whether the user is logged in or not. If the user isn't logged in, the 'Login' and 'Register' links are shown in the Bugs and Features cards. When the user is logged in, the links are replaced with buttons that allow users to log a new Bug Report or Feature Request.
- **Flash Messages** - Displayed at the top of the page below the navbar. These messages differ based on user interaction and provides helper messages for users. Each message is displayed for 3000 milliseconds.
- **Login** - Allows existing users to login to their account. The username field accepts either the username or email address associated with a particular account. I've included authorization checks to verify the username/email address and password against the details stored in the database before users can be logged in.
- **Register** - Allows new users to register for a free account. I've included checks to ensure that the username and email address don't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes. Upon successful registration, a default profile image is allocated to the user.
- **Logout** - Allows users to logout of their account by clicking the 'Logout' link in the navbar/sidenav. Upon clicking the button, the user session ends.
- **Reset Password** - Allows users to reset their password. Upon entering their email address, the user will receive an email containing a link to reset their password. The email link takes the user to a page where they can reset their password, providing the new password meets Django's standard requirements.
- **Profile Page** - When logged in, users can visit their profile page to view a list of their added tickets, add a profile picture, or edit other profile details.
- **Edit Profile** - In the user's profile page, the 'Edit Profile' button triggers a modal with a form. The form pre-populates the user's details, which they can edit. Users are also required to upload an image file for their profile image before the form can be submitted successfully.
- **Added Bugs/Features List** - In the user's profile page, the 'My Bugs' and 'My Features' sections display a list of the user's added tickets, separated into Bugs and Features. The user can click the ticket name or description to view the full details of that particular ticket. The user can also click the relevant links to add new Bug Reports or Feature Requests.
- **Tickets** - All tickets are initially displayed when the 'Tickets' page first loads. Tickets are displayed in descending order of the number of upvotes.
- **Filter** - Users can filter tickets based on up to 2 categories - ticket type and ticket status, and the results are subsequently displayed when the user clicks the Filter button. If the form is submitted without choosing any options, all the tickets are loaded. Filtered result are displayed in descending order of the number of upvotes.
- **Reset Button** - Clicking the 'Reset' button refreshes the 'Tickets' page and restores its default values.
- **Ticket Preview Cards** - Each preview card shows the relevant ticket's name and some quick stats (type, status, creator, description preview, number of views, number of likes and total donation). For bug tickets, the total donation section displays 'FREE!'. For features, this section displays the total donated amount, if the donation goal hasn't been met. If the donation goal has been met, the donation amount is replaced with a 'Tick' icon. Clicking the ticket card takes the user to that ticket's page with its full details.
- **Pagination** - The Tickets page uses pagination for both the unfiltered and filtered results to display 6 tickets per page. The first and previous page buttons are only available displayed if there is a first or previous page. The next and last page buttons are only available displayed if there is a next or last page.
- **Add Ticket** - Create operation. Allows the user to add a new ticket to the site and database. All form fields are required. Bug Reports are free to log. However, Feature Tickets require a donation amount, which can be chosen from the form's select menu. The user would then be required to complete the payment form to make the payment and add the Feature Request. The default status of all new tickets is set to 'Open'. However, if the user donates the goal amount (£100) when creating the Feature Request, the status is set to 'In Progress'. *_For this project's purpose, the form uses Stripe's test payment system_*.
- **View Full Ticket Details** - Read operation. Displays the ticket's full details on a page. If the ticket hasn't been edited, the added date is displayed. If it has been edited, the edited_date is displayed instead. For Features, the total amount donated is displayed. If the donation goal has been reached, the donation amount is replaced by, 'Donation Amount Reached'.
- **Super User Privileges** - Allows the super user (admin) to edit a ticket's status. A select menu in the 'Full Ticket Details' page allows the super user to select and update a ticket to a different status. When a ticket status is update, the edited_date is also updated with the current date.
- **Edit Ticket Button** - The 'Edit' button is available only when the user is logged in, and if they have created that particular ticket. Clicking it takes the user to the 'Edit Ticket' page.
- **Edit Ticket** - Update operation. The existing ticket values are pre-populated in the relevant form fields, which the user is able to edit if required. Upon form submission, the ticket database record is updated with the new values. Additionally, the edited_date field in the ticket record is updated with the current date.
- **Delete Ticket** - The 'Delete' button is only available if the user is logged in and they have added that ticket. Clicking the button triggers the 'Delete' modal, which asks the user to confirm the deletion request. If the user presses 'YES', the ticket's database record is removed from the database.
- **Upvote Ticket** - The 'Upvote' button is only available if the user is logged in, if they haven't created the ticket, and if the ticket status isn't 'Closed'. For all Bugs, and Features where the donation goal has been reached, the 'Upvote' button increments the ticket's upvote count by 1 and creates an 'Upvote' object for that particular user and ticket. For Features where the donation goal hasn't been met, the 'Donate & Upvote' button loads the payment modal, which allows the user to make a donation before their upvote is registered. Once a ticket is upvoted by the user, the button changes to a 'Downvote' button instead, which ensures the user can only upvote any ticket once.
- **Downvote Ticket** - The 'Downvote' button is only available if the user is logged in, if they haven't created the ticket, if the ticket isn't closed, and they have already upvoted the ticket. Clicking the button removes the 'Upvote' object that was created when the user upvoted the ticket, the ticket's upvotes value is decremented by -1, and the button changes back to 'Upvote'. The 'Downvote' button is disabled for Features, to ensure that the user can't downvote a Feature and make another donation.
- **Comments** - Allows the user to comment on a ticket. This form is only available if the user is logged in and the ticket isn't closed. The form field is required for successful form submission. Upon submission, the user's comment is displayed in the 'Comments' section, along with all other existing comments on the ticket.
- **Dashboard** - Displays some statistics relating to the site. All sections and charts are interactive. The helper text instructs the user to 'click' on each section on desktops, and to 'tap' on each section for tablets and mobiles.
- **Top 5...** - The 'Top 5...' section lists the top 5 most voted for Bugs and Features. The user can click on the relevant ticket's title or description to load the full details for that ticket.
- **Status** - The 'Status' bar chart separates the tickets into Bugs and Features, and shows the number of tickets at each status - Open, In Progress, or Closed.
- **Ticket Types** - The 'Ticket Types' bar chart gives a visual representation of the total number of each ticket type.
- **Cancel Buttons** - Cancels the relevant action and takes the user back to the previous page in their browsing history.
- **Custom Error Messages** - I've included custom 404 and 500 error messages and error handlers to catch these errors. My custom messages allow the user to re-navigate to any of the app's pages.

### Features Left to Implement

With more time and knowledge, I would like to implement some additional features to the app:

- **Search By Name** - Users can currently only filter tickets based on 2 categories. Given more time, I would like to implement a search functionality which allows users to search for a ticket by its name or a keyword.
- **Points For Activities** - With more Django knowledge, I would like to implement a points system where users can score points for various activities - ticket submissions, upvotes, donations and comments. These points could then unlock perks, such as being able to donate more than once on a Feature, or upvote a ticket more than once.
- **Report To Admin** - With more knowledge, I would like to implement a feature which allows users to report malicious content or abusive behaviour by other users to the admin.
- **Delete Profile** - With more time, I would like to implement the ability for users to delete their profile. Deleting a profile could then delete all the user's existing ticket records from the database.
- **Additional Graph** - With more time, I would like to add an additional graph to show how many tickets were opened or worked on and closed per day/week/month.

## Technologies Used

- [**Balsamiq**](https://balsamiq.com/)
    - I've used **Balsamiq** to create wireframes of my website/app before building it.
- [**Visual Paradigm**](https://www.visual-paradigm.com/)
    - I've used **Visual Paradigm** to create the ER diagram for my Database Schema before building my project.
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles to the elements and content of my app. The base.html file is linked directly to the custom.css stylesheet.
- [**Materialize**](https://materializecss.com/)
    - The project uses the **Materialize** framework to add a responsive grid system, prebuilt components, plugins built on jQuery, and Materialize styles to my app, before adding my custom styles.
- [**jQuery**](https://jquery.com)
    - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file.
- [**Python**](https://www.python.org/)
    - The project uses **Python** as the back-end programming language for my app.
- [**Django**](https://www.djangoproject.com/)
    - The project uses **Django** as the Python web framework.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Python and Django in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**Stripe API**](https://stripe.com/gb)
    - The project uses **Stripe** to make secure payments for logging and upvoting Feature Requests. The project uses Stripe's test payment functionality.
- [**C3.js**](https://c3js.org/)
    - The project uses **C3.js** to render interactive charts and graphs for the dashboard.
- [**SQLite**](https://www.sqlite.org/index.html)
    - The project uses **SQLite** as the relational database to hold the backend information for the varions models used, when running locally.
- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used, when deployed remotely.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Open Sans_* font and the rest of the site uses the *_Roboto_* font.
- [**Font Awesome**](https://fontawesome.com/)
    - The project uses **Font Awesome** for the various icons in my app.
- [**AWS Educate Cloud9**](https://aws.amazon.com/education/awseducate/)
    - I've used **AWS Educate Cloud9** as the development environment to write the code for my website.

### Version Control

- [**Git**](https://git-scm.com/)
    - I've used **Git** as a version control system to regularly add and commit changes made to project in AWS Educate Cloud9, before pushing them to GitHub.
- [**GitHub**](https://github.com/)
    - I've used **GitHub** as a remote repository to push and store the committed changes to my project from Git.

### Hosting

- [**Heroku**](https://www.heroku.com/)
    - I've used **Heroku** as the hosting platform to deploy my app.

## Testing

### Testing User Stories

I used my user stories and documented each of the steps that each user would need to complete to accomplish what they have stated. Below is the link to the document that contains this information:

- [Testing User Stories](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/testing/testing-user-stories.pdf)

### Responsive and Functional Testing

I used Google Chrome's Development tools to constantly test each change that I made to my project and to ensure that it appeared in the desired way on different screen sizes. I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure it appeared in the desired way on different devices.

I created my own account and some fake user accounts to test the functionality and validation worked as expected.

To test my whole app, I went through each feature and documented the results on a spreadsheet. The spreadsheet also documents any responsive features and confirms that they work and appear as intended on different screen sizes. The link to the spreadsheet is below:

- [Testing Checklist](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/testing/testing-checklist.pdf)

### Additional Testing

In addition to my own testing, I also asked family members, friends and the Slack community to test my app and provide any feedback.

### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

### Automated Testing

I wrote various tests to automate certain forms and views used in my project using Django's `unittest` library. All tests pass.

The tests provide an overall coverage of 34%. However, given more time and knowledge around Django testing, I would like to improve the coverage to the approved minimum requirement of 75%.

### Travis Continuous Integration

In addition to the automated testing files, I used [Travis CI](https://travis-ci.org/) for Continuous Integration testing of my code.

I had an issue with two of my automated tests for the `UserUpdateForm` and `ProfileUpdateForm` in the `test_forms.py` file in the `accounts` app. Travis was throwing an error when running these tests, as there were no environment variables set in the Travis environment. I got some advice from the Code Institute Tutor team and was advised to comment out the two tests and include an explanation for the reason in both the relevant file, and also my README.md file.

### Interesting Bugs Or Problems

- **Profile Creation When Registering User** - I followed a video tutorial to create a profile when registering a user, and to allow them to update their profile picture. The feature worked fine initially, but then I kept getting an error when registering a new user. I resolved this by inserting additional arguments in the `save` function in the Profile model, as advised by a [Django TypeError](https://stackoverflow.com/questions/52351756/django-typeerror-save-got-an-unexpected-keyword-argument-force-insert/52351829) article on StackOverflow. The feature now works as intended.
- **Unable To Migrate Databases** - After making a few changes to my models, I kept getting an error when I tried to run the `python3 manage.py makemigrations` and `python3 manage.py migrate` to migrate my database models. I resolved this by deleting the `__pycache__` and `migrations` folders in all apps that contained models, as advised by a [Django No Such Table Exception](https://stackoverflow.com/questions/34548768/django-no-such-table-exception) article on StackOverflow.
- **Pagination Not Working On Filtered Results** - When loading the next page or a particular page of the filtered result, this brought up the relevant page of the default values (all tickets) instead of that of the filtered results. I resolved this by creating a template tag within the `tickets` app and injecting it into the relevant HTML file to allow the page parameters to be remembered, as advised by a [Django Filtering And Pagination](https://www.caktusgroup.com/blog/2018/10/18/filtering-and-pagination-django/) article.
- **Allowed Users To Pay Again When Feature Downvoted** - If the user paid to upvote a feature and they then downvoted it, the 'Donate & Upvote' button would be displayed again if the donation goal hadn't been met. This would then allow the same user to make another donation and upvote the ticket again. I only wanted a particular user to be able to make a donation to upvote a Feature ticket once, and not multiple times. To resolve this issue, I disabled the 'Downvote' button on Feature Requests.
- **Reset Password** - Despite allowing less secure apps within my Google Account settings, as instructed by Code Institute's LMS videos, I was still getting an `SMTPAuthenticationError` when entering the password on the 'Password Reset' screen. This meant that the site was failing to send the password reset email to the user. I resolved this issue by activating the 2-Step Authentication in my Google Account, creating an app password and storing it within my environment variables instead of my standard GMail password, as instructed by the [Django SMTPAuthenticationError](https://stackoverflow.com/questions/26697565/django-smtpauthenticationerror) article.
- **Image Not Saving To Direct Path In PostgreSQL** - After deploying my site in the live environment and linking it to Heroku's PostgreSQL Add-On and my AWS S3 Bucket, I kept getting an error when trying to register a new user, or upload the image of an existing user, stating that PostgreSQL could not save the file to an absolute file path. I resolved the issue by amending some settings in the `save` function in the Profile model, as advised by the [Django Storage NotImplementedError](http://blog.hardlycode.com/solving-django-storage-notimplementederror-2011-01/) and [Getting PIL Image Save Method To Work With Amazon S3boto Storage](https://stackoverflow.com/questions/14680323/django-getting-pil-image-save-method-to-work-with-amazon-s3boto-storage/14681113#14681113) articles.

## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Went to the **Resources** tab in Heroku and searched for **Heroku Postgres** in the 'Add-Ons' section.
3. Selected the free **Hobby** level.
4. Updated the `.bashrc` file within my local workspace with the `DATABASE_URL` details, and the `settings.py` to connect to the database using the `dj_database_url` package.
5. Ran the `python3 manage.py makemigrations`, `python3 manage.py migrate`, `python3 manage.py createsuperuser` commands to migrate the models into Heroku Postgres and create a new super user in the new PostgreSQL database.
5. Went to the **Settings** tab in Heroku and clicked on the **Reveal Config Vars** button.
6. Copied and pasted all of the `.bashrc` default variables in Heroku's Config Vars section.
7. Went to the **Deploy** tab in Heroku, connected my app to my GitHub repository and selected **Enable Automatic Deployment** as the deployment method.
8. Went to the **Developers** section in Stripe and clicked on **API Keys**.
9. Copied and pasted the **Publishable Key** and **Secret Key** and set them as the `STRIPE_PUBLISHABLE` and `STRIPE_SECRET` environment variables in the `.bashrc` file within my local workspace.
10. Updated the `settings.py` with the new Stripe environment variables.
8. Went to the **S3** section of AWS and created a new S3 bucket.
9. Within the relevant bucket's permissions, changed the **CORS Configuration** to the following:

    ```
    <?xml version="1.0" encoding="UTF-8"?>
    <CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
    </CORSConfiguration>
    ```

10. Still in the **S3** section, changed the **Bucket Policy** to the following:

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::<my-bucket-name>/*"
            }
        ]
    }
    ```

11. Replaced the `<my-bucket-name>` in the `Resource` line with my S3 bucket's name instead.
12. Went to the **IAM** section of AWS, created a 'New Group' and attached my S3 bucket details to it.
13. Still in the **IAM** section, created a 'New Policy' and a 'New User' and attached these to the newly created group.
14. Updated the `settings.py` file in my local workspace with the relevant S3 bucket details:

    ```
    AWS_S3_OBJECT_PARAMETERS = {
        "Expires": "Thu, 31 Dec 2099 20:00:00 GMT",
        "CacheControl": "max-age=94608000",
    }
    AWS_STORAGE_BUCKET_NAME = "<s3-bucket-name>"
    AWS_S3_REGION_NAME = "<region-name>"
    AWS_ACCESS_KEY_ID = <access-key-id>
    AWS_SECRET_ACCESS_KEY = <secret-access-key>
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = None
    ```

15. Created a `custom_storages.py` file with classes to route to the relevant location settings for static and media files.
16. Updated the `settings.py` file with the relevant configuration for static and media file storage.
17. Ran the `python3 manage.py collectstatic` command to push the static files to my S3 bucket.
18. Created a requirements.txt file using the following command in the terminal window:

    ```sudo pip3 freeze --local > requirements.txt```

19. Created a Procfile using the following command in the terminal window:

    ```echo web: gunicorn UnicornAttractor.wsgi:application > Procfile```

20. Ran the `git add .`, `git commit -m "<commit-message>"` and `git push` commands to push all changes to my GitHub repository.

The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[UnicornAttractor](https://unicorn-attractor-ms4-hebs87.herokuapp.com/)

### Repository Link

Click the link below to visit my project's GitHub repository:

[UnicornAttractor GitHub Repository](https://github.com/hebs87/unicorn-attractor-milestone-four)

### Running Code Locally

To run my code locally, users can download a local copy of my code to their desktop by completing the following steps:

1. Go to [my GitHub repository](https://github.com/hebs87/unicorn-attractor-milestone-four)
2. Click on 'Clone or download' under the repository name.
3. Copy the clone URL for the repository in the 'Clone with HTTPs section'.
4. Open 'Git Bash' in your local IDE.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, then paste the URL you copied in Step 3:

    ```git clone https://github.com/USERNAME/REPOSITORY```

7. Press `Enter` to complete the process and create your local clone.
8. Complete one of the two below steps in your local workspace to set your own credentials for the environment variables:
    - Enter and save your own credentials in the `.baschrc` file; or
    - Create a `.env,py` file with your own credentials and import this into the `settings.py` file
9. Install the `requirements.txt` file by running the below command in your CLI Terminal:

    ```sudo pip3 install -r requirements.txt```

10. Run one of the following commands in your Terminal to launch the Django project:

    ```python3 manage.py runserver```

11. Click the `http://` link that loads, and the project should load. If it doesn't load when you click the link, copy and paste it into a new browser tab instead.
12. Run the following commands to migrate the database models and create a super user:

    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    ```

Once the migrations are completed and the super user has been created successfully, the site should be running locally. To deploy the site remotely, follow the instructions in the [Deployment](#Deployment) section.

### Media And Static Folders

During development, my `static` and `media` folders weren't pushed to GitHub at any stage, as instructed in the Code Institute LMS lessons. These folders were added to my `.gitignore` file, as they are hosted in my S3 bucket for the live version of the site.

I pushed these folders to GitHub and commented them out of the `.gitignore` file just before submitting my project, purely for the purpose of assessment.

## Credits

### Content

- All of the code for my project was written by me.
- I researched how to link Django forms to Materialize by reading the [Django MaterializeCSS Form](https://pypi.org/project/django-materializecss-form/) documentation.
- I used the [Django Secret Key Generator](https://www.miniwebtool.com/django-secret-key-generator/) to generate the secret key for my project.
- I used some example code from the [User Profile And Picture](https://www.youtube.com/watch?v=FdVuKt_iuSI) and [Update User Profile](https://www.youtube.com/watch?v=CQ90L5jfldw&t=546s) videos to help create the functionality for creating a User Profile upon registration, and to allow the user to update their profile picture and details.
- I reasearched how to delete old images when the user uploads a new Profile image by reading the [django_cleanup](https://stackoverflow.com/questions/2878490/how-to-delete-old-image-when-update-imagefield) article.
- I found out how to add the current date to a model field by reading the [Automatic Creation Date](https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects) article on StackOverflow.
- I researched how to filter based on choice form options by watching [Filter Video 1](https://www.youtube.com/watch?v=V-xXdsi91wc) and [Filter Video 2](https://www.youtube.com/watch?v=GtwK0Hj6jU8&t=180s). These videos also inspired my database schema and the models that I used in the `tickets` app.
- I researched how to implement pagination, and how to make it work with the filtered results by reading the [Pagination](https://docs.djangoproject.com/en/2.2/topics/pagination/) and [How To Paginate With Django](https://simpleisbetterthancomplex.com/tutorial/2016/08/03/how-to-paginate-with-django.html) articles, and watching the [Pagination](https://www.youtube.com/watch?v=acOktTcTVEQ) video.
- I reasearched how to create and delete an upvote object when the user upvotes or downvotes a ticket by reading the [Queries](https://docs.djangoproject.com/en/2.2/topics/db/queries/) article.
- I researched how to format dates in Jinja by reading the [Templates - Date](https://docs.djangoproject.com/en/2.2/ref/templates/builtins/#date) article.
- I researched how to change Django form labels to icons by reading the [How To Have A Link In Label Of A Form Field](https://stackoverflow.com/questions/386042/how-to-have-a-link-in-label-of-a-form-field) article on StackOverflow. This helped me to change the image file upload field label to an icon instead.
- I read the [C3.js](https://c3js.org/) documentation to learn how to render the graphs used in my dashboard in a HTML template.
- I researched how to filter and sort the top 5 most voted for tickets by reading the [Query For Top X Elements In Django](https://stackoverflow.com/questions/6436937/query-for-top-x-elements-in-django) article.
- I learnt how to create custom error handlers by reading the [Creating Custom Error Pages](https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page/24725091) article in StackOverflow. I also read the [Return 404 Page Intentionally](https://stackoverflow.com/questions/49465281/how-to-return-404-page-intentionally-in-django) article to test my `404` error handler.
- I researched how to write a unittest for a file upload by reading the [Unit Test File Upload](https://stackoverflow.com/questions/11170425/how-to-unit-test-file-upload-in-django) article. This test is commented out as it caused Travis compatibility issues.

### Media

- I found the Favicon image on Google, and I used the [Favicon Converter](https://favicon.io/favicon-converter/) to convert the image to a Favicon.
- I found the site's logo on Google.
- The images for the User Profile images were my own pictures.

### Acknowledgements

- Thanks to the Code Institute Tutors who helped me to troubleshoot some issues with AWS Cloud9.
- Thanks to the Slack community for their helfpul feedback.
- A special mention to my mentor, Dick Vlaanderen, for his feedback on my project's scope, design and functionality.

### Disclaimer

This project is for educational purposes only.