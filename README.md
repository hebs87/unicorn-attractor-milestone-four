# [UnicornAttractor]() - Milestone Project Four

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

I created this app for the Full Stack Frameworks project of [**_Code Institute's_**](https://codeinstitute.net/) Full Stack Software Development course. The project scope was to ...

The front-end display and functionality uses HTML, CSS and JavaScript. The back-end functionality uses Python, Django, SQLite3 and PostgreSQL.

## UX

### User Stories



### Style Rationale

I received inspiration for the style of my app ...

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



### Existing Features



### Features Left to Implement

With more time and knowledge, I would like to implement some additional features to the app.



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
- [**PyMongo**](https://api.mongodb.com/python/current/)
    - The project uses **PyMongo** as the Python API for MongoDB. This API enables linking the data from the back-end database to the front-end app.
- [**Flask**](https://flask.palletsprojects.com/en/1.0.x/)
    - The project uses **Flask**, which is a Python microframework.
- [**Flask Blueprint**](https://flask.palletsprojects.com/en/1.0.x/blueprints/)
    - The project user **Flask Blueprint** to compartmentalise my Python code and make it more modular and easier to navigate.
- [**Jinja**](https://jinja.palletsprojects.com/en/2.10.x/)
    - The project uses **Jinja** for templating with Flask in the HTML code. I used **Jinja** to simplify my HTML code, avoid repetition, and allow simpler linking of the back-end to the front-end.
- [**MongoDB**](https://cloud.mongodb.com/)
    - The project uses **MongoDB** to store the database in the cloud. The information displayed in the front-end app is pulled from the database store.
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

- [Testing User Stories]()

### Responsive and Functional Testing

I used Google Chrome's Development tools to constantly test each change that I made to my project and to ensure that it appeared in the desired way on different screen sizes. I also tested my app on different screen sizes (mobile, tablet and desktop) to ensure it appeared in the desired way on different devices.

I created my own account and several fake user accounts to test the functionality and validation worked as expected.

To test my whole app, I went through each feature and documented the results on a spreadsheet. The spreadsheet also documents any responsive features and confirms that they work and appear as intended on different screen sizes. The link to the spreadsheet it below:

- [Testing Checklist]()

### Additional Testing

In addition to my own testing, I also asked family members, friends and the Slack community to test my app and provide any feedback.

### Code Validation

- I used the [W3C HTML Validator tool](https://validator.w3.org/#validate_by_input) to validate my HTML code.
    - The W3C Validator tool doesn't recognise the Jinja templating, which has resulted in it showing a lot of errors in relation to the Jinja code. However, all other code is validating fine.
- I used the [W3C CSS Validator tool](https://jigsaw.w3.org/css-validator/#validate_by_input) to validate my CSS code.
- I used the [Esprima Syntax Validator tool](http://esprima.org/demo/validate.html) to validate my JavaScript syntax.
- I used the [Pep8 Online tool](http://pep8online.com/) to validate my Python syntax.

### Automated Testing



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