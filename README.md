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
  - [Interesting Bugs Or Problems](#Interesting-Bugs-Or-Problems)
    - [Resolved Bugs](#Resolved-Bugs)
    - [Partially Resolved or Unresolved Bugs](#Partially-Resolved-or-Unresolved-Bugs)
- [**Deployment**](#Deployment)
  - [Live App Link](#Live-App-Link)
  - [Repository Link](#Repository-Link)
  - [Running Code Locally](#Running-Code-Locally)
- [**Credits**](#Credits)
  - [Content](#Content)
  - [Acknowledgements](#Acknowledgements)
  - [Disclaimer](#Disclaimer)

## About

This application (app) is ...

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

Before building my project, I created an Entity Relationship (ER) diagram to outline the database schema for the various tables that I would use. The links to the file below:

- [UnicornAttractor Database Schema](https://github.com/hebs87/unicorn-attractor-milestone-four/blob/master/design/schema/unicorn-attractor-db-schema.pdf)

## Features

### Functionality

The app uses Python logic to allow users to login, or register for a free account. The app offers CRUD operations to allow users to create, read, update and delete tickets. Users can filter tickets based on various categories. Additionally, users can upvote or downvote tickets - upvoting feature tickets requires a small donation.

I added some additional features that weren't within the scope of the project, as I felt that they offered better interactivity for users.

### Existing Features

- **Navbar/Sidenav Links** - The navbar and sidnav links vary depending on whether the user is logged in or not. If the user isn't logged in, the Home, Tickets, Login and Register links are shown. When the user is logged in, the Home, Tickets, Profile and Logout links are shown.
- **App Store/Google Play Buttons** - The App Store button loads the Apple App store in a new browser tab. The Google Play button loads the Google Play store in a new browser tab. While the UnicornAttractor app isn't actually a real app available for download, this creates authentcity for the user by giving them the impression that they can download it.
- **Index Links/Buttons** - The links and buttons on the index page vary depending on whether the user is logged in or not. If the user isn't logged in, the Login and Register links are shown in the Bugs and Features cards. When the user is logged in, the links are replaced with buttons that allow users to log a new Bug Report or Feature Request.
- **Flash Messages** - Displayed at the top of the page below the navbar. These messages differ based on user interaction and provides helper messages for users. Each message is displayed for 3000 milliseconds.
- **Login** - Allows existing users to login to their account. The username field accepts either the username or email address associated with a particular account. I've included authorization checks to verify the username/email address and password against the details stored in the database before users can be logged in.
- **Register** - Allows new users to register for a free account. I've included checks to ensure that the username and email address don't already exist in the database before users are successfully registered. The passwords stored in the database are hashed for security purposes. Upon successful registration, a default profile image is allocated to the user.
- **Logout** - Allows users to logout of their account by clicking the 'Logout' link in the navbar/sidenav. Upon clicking the button, the user session ends.
- **Reset Password** - Allows users to reset their password. Upon entering their email address, the user will recieve an email containing a link to reset their password. The email link takes the user to a page where they can reset their password, providing the new password meets Django's standard requirements.
- **Profile Page** - When logged in, users can visit their profile page to view a list of their added tickets, add a profile picture, or edit other profile details.
- **Edit Profile** - In the user's profile page, the 'Edit Profile' button triggers a modal with a form. The form pre-populates the user's details, which they can edit. Users are also required to upload an image file for their profile image before the form can be submitted successfully.
- **Added Bugs/Features List** - In the user's profile page, the 'My Bugs' and 'My Features' sections display a list of the user's added tickets, separated into Bugs and Features. The user can click the ticket name or description to view the full details of that particular ticket. The user can also click the relevant links to add new Bug Reports or Feature Requests.
- **Tickets** - All tickets are initially displayed when the 'Tickets' page first loads. Tickets are displayed in descending order of the number of upvotes.
- **Filter** - Users can filter tickets based on up to 2 categories - ticket type and ticket status, and the results are subsequently displayed when the user clicks the Filter button. If the form is submitted without choosing any options, all the tickets are loaded. Filtered result are displayed in descending order of the number of upvotes.
- **Reset Button** - Clicking the Reset button refreshes the 'Tickets' page and restores its default values.
- **Ticket Preview Cards** - Each preview card shows the relevant ticket's name and some quick stats (type, status, creator, description preview, number of views, number of likes and total donation). For bug tickets, the total donation section displays 'FREE'. For features, this section displays the total donated amount if the donation goal hasn't been met. If the donation goal has been met, the donation amount is replaced with a 'Tick' icon. Clicking the ticket card takes the user to that ticket's page with its full details.
- **Pagination** - The Tickets page uses pagination for both the unfiltered and filtered results to display 6 tickets per page. The previous page button is only available if there is a previous page. The next page button is only available if there is a next page.
- **Add Ticket** - Create operation. Allows the user to add a new ticket to the site and database. All form fields are required. Bug Reports are free to log. However, Feature Tickets require a donation amount, which can be chosen from the form's select menu. The user would then be required to complete the payment form to make the payment and add the Feature Request. The default status of all new tickets is set to 'Open'. However, if the user donates the goal amount (£100) when creating the Feature Request, the status is set to 'In Progress'. *_For this project's purpose, the form uses Stripe's test payment system_*.
- **View Full Ticket Details** - Read operation. Displays the ticket's full details on a page. If the ticket hasn't been edited, the added date is displayed. If it has been edited, the edited_date is displayed instead. For Features, the total amount donated is displayed. If the donation goal has been reached, the donation amount is replaced by, 'Donation Amount Reached'.
- **Super User Priveleges** - Allows the super user (admin) to edit a ticket's status. A select menu in the Full Ticket Details page allows the super user to select and update a ticket to a different status. When a ticket status is update, the edited_date is also updated with the current date.
- **Edit Ticket Button** - The Edit button is available only when the user is logged in, and if they have created that particular ticket. Clicking it takes the user to the Edit Ticket page.
- **Edit Ticket** - Update operation. The existing ticket values are pre-populated in the relevant form fields, which the user is able to edit if required. Upon form submission, the ticket database record is updated with the new values. Additionally, the edited_date field in the ticket record is updated with the current date.
- **Delete Ticket** - The Delete button is only available if the user is logged in and they have added that ticket. Clicking the button triggers the Delete modal, which asks the user to confirm the deletion request. If the user presses 'YES', the ticket's database record is removed from the database.
- **Upvote Ticket** - The Upvote button is only available if the user is logged in, if they haven't created the ticket, and if the ticket status isn't 'Closed'. For all Bugs, and Features where the donation goal has been reached, the Upvote button increments the ticket's upvote count by 1 and created an 'Upvote' object for that particular user and ticket. For Features where the donation goal hasn't been met, the 'Donate & Upvote' button loads the payment modal, which allows the user to make a donation before their upvote is registered. Once a ticket is upvoted by the user, the button changes to a 'Downvote' button instead, which ensures the user can only upvote any ticket once.
- **Downvote Ticket** - The Downvote button is only available if the user is logged in, if they haven't created the ticket, if the ticket isn't closed, and they have already upvoted the ticket. Clicking the button removes the 'Upvote' object that was created when the user upvoted the ticket, the ticket's upvotes value is decremented by -1, and the button changes back to 'Upvote'. The Downvote button is disabled for Features, to ensure that the user can't downvote a Feature and make another donation.
- **Comments** - Allows the user to comment on a ticket. This form is only available if the user is logged in and the ticket isn't closed. The form field is required for successful form submission. Upon submission, the user's comment is displayed in the 'Comments' section, along with all other existing comments on the ticket.
- **Dashboard** - Displays some statistics relating to the site. All sections and charts are interactive. The helper text instructs the user to 'click' on each section on desktops, and to 'tap' on each section for tablets and mobiles.
- **Top 5...** - The 'Top 5...' section lists the top 5 most voted for Bugs and Features. The user can click on the relevant ticket's title or description to load the full details for that ticket.
- **Status** - The Status bar chart separates the tickets into Bugs and Features, and shows the number of tickets at each status - Open, In Progress, or Closed.
- **Ticket Types** - The Ticket Types bar chart gives a visual representation of the total number of each ticket type.
- **Cancel Buttons** - Cancels the relevant action and takes the user back to the previous page in their browsing history.
- **Custom Error Messages** - I've included custom 404 and 500 error messages and error handlers to catch these errors. My custom messages allow the user to re-navigate to any of the app's pages.

### Features Left to Implement

With more time and knowledge, I would like to implement some additional features to the app.

- **Search By Name** - Users can currently only filter tickets based on 2 categories. Given more time, I would like to implement a search functionality which allows users to search for a ticket by its name or a keyword.
- **Points For Activities** - With more Django knowledge, I would like to implement a points system where users can score points for various activities - ticket submissions, upvotes, donations and comments. These points could then unlock perks, such as being able to donate more than once on a Feature, or upvote a ticket more than once.
- **Report To Admin** - With more knowledge, I would like to implement a feature which allows users to report malicious content or abusive behaviour by other users to the admin.
- **Delete Profile** - With more time, I would like to implement the ability for users to delete their profile. Deleting a profile could then delete all the user's existing ticket records from the database.
- **Additional Graph** - With more time, I would like to add an additional graph to show how many tickets were opened or worked on and closed per day/week/month.

## Technologies Used

- [**Balsamiq**](https://balsamiq.com/)
    - I've used **Balsamiq** to create wireframes of my website/app before building it.
- [**HTML**](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
    - The project uses **HTML** to create the basic elements and content of my app.
- [**SCSS**](https://sass-lang.com/documentation/syntax)
    - The project uses **SCSS** to add custom styles to the elements and content of my app. I used **SCSS** instead of **CSS**, as it is more powerful and I used the logic to write some variables, mixins and media queries, which I called for various features.
- [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
    - The project uses **CSS** to apply the custom styles created with **SCSS** to my app. The base.html file is linked directly to the main.min.css stylesheet.
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
- [**PostgreSQL**](https://www.postgresql.org/)
    - The project uses Heroku's **PostgreSQL** relational database to hold the backend information for the various models used in the project.
- [**Google Fonts**](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the text and suit my chosen theme. The brand logo uses the *_Dancing Script_* font and the rest of the site uses the *_Roboto_* font.
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

To test my whole app, I went through each feature and documented the results on a spreadsheet. The spreadsheet also documents any responsive features and confirms that they work and appear as intended on different screen sizes. The link to the spreadsheet it below:

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

### Travis Continuous Integration (CI)

In addition to the automated testing files, I used [Travis CI](https://travis-ci.org/) for CI testing of my code.

I had an issue with two of my automated tests for the `UserUpdateForm` and `ProfileUpdateForm` in the `test_forms.py` file in the `accounts` app. Travis was throwing an error when running these tests, as there were no environment variables set in the Travis environment. I got some advise from the Code Institute Tutor team and was advised to comment out the two tests and include an explanation for the reason in both the relevant file, and also my README.md file.

### Interesting Bugs Or Problems



#### Resolved Bugs



#### Partially Resolved or Unresolved Bugs



## Deployment

I used GitHub for my version control and Heroku to host the live version of my project. To deploy my website to Heroku, I used the following steps:

1. Created the app in Heroku.
2. Ran the `sudo snap install --classic heroku` command in the terminal window to instal heroku in my local workspace.
3. Ran the `heroku login --interactive` command in the terminal window and entered my credentials to login to Heroku.
4. Added and committed the files to Git using the `git add .` and `git commit -m ""` commands in the terminal window.
5. Linked the Heroku app as the remote master branch using the following command in the terminal window:

    ```heroku git:remote -a <app-name>```

6. Created a requirements.txt file using the following command in the terminal window:

    ```sudo pip3 freeze --local > requirements.txt```

7. Created a Procfile using the following command in the terminal window:



8. Ran the `git push heroku master` command in the terminal window to push the app to Heroku.
10. Entered the following Config Vars in Heroku:



The app was successfully deployed to Heroku at this stage.

### Live App Link

Click the link below to run my project in the live environment:

[UnicornAttractor]()

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

## Credits

### Content

- All of the code for my project was written by me.

### Media

- I found the Favicon image on Google, and I used the [Favicon Converter](https://favicon.io/favicon-converter/) to convert the image to a Favicon.

### Acknowledgements

- I received inspiration for the style of my project from []().
- Thanks to the Slack community for their feedback, and for .
- A special mention to my mentor, Dick Vlaanderen, for his feedback on my project's scope, design and functionality.

### Disclaimer

This project is for educational purposes only.