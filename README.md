# Developer: Marius Emanuel Nicusor
# Store Management App

The Store Management App was created as Portfolio Project #3 (Python Essentials) for Diploma in Full Stack Software Development at Code Institute. It allows users to simulate/manage an online shoping cart while they can view products, add to cart, remove from cart,apply discounts, pay and print receipts.

Project purpose was to build a command-line python application that allows user to manage a common dataset about a particular domain.

# Table of content

1. [Project](1-#project)
    *   [Strategy/Scope](#strategyscope)
    *   [Site owner goals](#site-owner-goals)
    *   [External user's goal](#external-users-goal)
2. [User Experience (UX/UI)](2-#user-experience-ux)
    *   [Colour Scheme](#colour-scheme)
3. [Logic and features](3-#logic-and-features)
    *   [Database structure](#database-structure)
    *   [Features](#features)
        *   [Main menu](#main-menu)
        *   [View products](#view-products)
        *   [Buy item](#buy-item)
        *   [Return item](#return-item)
        *   [View cart](#view-cart)
        *   [Apply discounts](#apply-discounts)
        *   [Pay and print receipts](#pay-and-print-receipts)
        *   [Quit](#quit)
4. [Technology](4-#technology)
    *   [Software used](#software-used)
    *   [Python libraries/modules](#python-librariesmodules)
5. [Testing](5-#testing)
    *   [Accessibility](#accessibility)
    *   [Validation](#validation)
    *   [Manual testing](#manual-testing)
    *   [Bugs/known issues](#bugsknown-issues)
6. [Deployment](6-#deployment)
    *   [Git and GitHub](#git-and-github)
    *   [Deployment to Heroku](#deployment-to-heroku)
7. [Possible future development](7-#possible-future-development)
8. [Credits](8-#credits)
    *   [Code](#code)
    *   [Media](#media)
    *   [Acknowledgements](#acknowledgements)

# 1. Project
##  Strategy/Scope

I chose to develop an application that can be used in real life. Store Management allows users to manage a dataset online grocery shop. Application offers such functionalities as: viewing grocery shop products, adding/returning, view cart, adding discounts, pay and print receipts and quit terminal.

Application should have clean and intuitive user interface and offer easy access and navigation to all functionalities.

To achieve the strategy goals I implemented following features:

- clean user interface for easy navigation and readability
- menu with easy acces to all features and possibility to exit program
- reliable and quick connection with database provided by Google
- customised terminal display page for better visual experience

## Site owner goals

As a program owner/developer I would like to:
- create application that has real life usage
- create application that is easy to use and intuitive to navigate
- create application with clean, good looking and accesible interface
- decide what kind of user input is allowed and valid
- create bug free application.

##  External user's goal

As a user I would like to:
- be able to clearly understand application purpose from the first contact
- be able to use program in real life
- be able to easily navigate the program and access all features
- be able to decide what to do next, what features to use
- be able to quit program
- avoid any errors/bugs during using the app

# 2.  User Experience (UX)
##  Colour Scheme
Colour of the "run program" button was adjusted to match the backgroud.

Terminal outputs are displayed in various colours over black background for better readability and accesibillity. 

Screenshots presenting terminal and colour outputs are available in [Features](#features) section.

Starting screen of the app with logo and menu:

# Logic and features


## Database structure

Google Sheets service is used to store project's database in the spreadsheet. There are two worksheets, one to store store products and second to store information about sorting methods.

Worksheet "library" is used to store book entries:

![database](docs/img/database.png)

Main table consists of six colums: ID, title, author, category, status and description. The ID value works as a ordinal number for database. It's not unique and fix value assigned to a book.

Each column has individually assigned value that represents maximum length of the string that can be input by user. It's 2, 24, 18, 12, 8 and 200 characters respectively. Exceeding that limit results in error and feedback sent to the user. This limitation is necessary to correctly display the table in the terminal which maximum length is 80 characters.  

The ID column value is assigned automatically when new book is added and also all ID values are renumbered when book is removed.

Worksheet "config" is used to store values for default and optional sorting method:

![config](docs/img/config.png)

