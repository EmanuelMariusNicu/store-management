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
        *   [Show total/admin use](#show-totaladmin-use)
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

Google Sheets service is used to store project's database in the spreadsheet. There are three worksheets, one to store grocery store products, second to store cart products and last sheet information about receipts.

Worksheet "library" is used to store book entry
Main table consists of three colums: products, price and quantity. 
![image](https://user-images.githubusercontent.com/108750655/209533713-378568a9-1269-4298-a6fd-71e23046025a.png)  

The cart google sheet is automated populated once customer buy products.
![image](https://user-images.githubusercontent.com/108750655/209534415-01ef474d-ed06-4c2e-8682-f41c1dd0d16f.png)


The receipts google sheet is only available for admin when using "7. Show total receipts" from main menu.
![image](https://user-images.githubusercontent.com/108750655/209534704-73ffbbec-bf1e-410a-a969-d496bef7d4f3.png)

## Features

### Main menu

Start screen of the application consists of ASCII logo, welcome message and main menu with 8 options. User input is validated.

![image](https://user-images.githubusercontent.com/108750655/209536228-fc098d8b-4de1-4c49-a211-fb4f032f1111.png)


### View products

This feature allows user to view products that are available and products that are out of stock. User can see product name, price and quantity available.
![image](https://user-images.githubusercontent.com/108750655/209536579-e943f680-863a-477b-ab3a-b1489c0ed333.png)

### Buy item

This function allows user to buy products. 
When using buy item user will have to type product name in order to add it to the cart.
![image](https://user-images.githubusercontent.com/108750655/209536970-4c5f6361-b681-4968-b57f-fad3194c5a65.png)
After buying first product than will get a message if he wants to continue shopping or no. 
![image](https://user-images.githubusercontent.com/108750655/209537268-92a28d80-b4cc-41d1-bdb3-9c400f97b0cf.png)
If user press "no" will be redirected to main menu.If user press "yes" will can continue shopping. If user type something different than product name will get a message to "choose another product".
![image](https://user-images.githubusercontent.com/108750655/209537590-67d4dc59-a58a-4782-af2d-4cc488dc315e.png)



### Return item

This function allows user to delete product from cart. User is asked to type what item he wants to return. The input is validated.
![image](https://user-images.githubusercontent.com/108750655/209538169-1c5cd3cb-5a7a-430a-a6fb-6628f01264cf.png)


If user write something different from what is inside cart will get a message like this.![image](https://user-images.githubusercontent.com/108750655/209538094-0cb42de5-9b83-486b-ac2d-22d05dad32d7.png)


### View cart

This function allows user to view all products from the cart.
![image](https://user-images.githubusercontent.com/108750655/209538372-8c04e11d-c125-4454-a218-87e31b8651ed.png)


### Apply discounts

This feature allows user to choose a discount option from "Apply Discount Menu". User has 4 options. 
![image](https://user-images.githubusercontent.com/108750655/209538829-4effaf58-6dcd-4f41-8c5f-fa9440e75dc4.png)

### Pay and print receipts

This function allows user make payment for all the products in the cart.
![image](https://user-images.githubusercontent.com/108750655/209540000-ddc83a6a-f92e-4537-931c-c2d32ed681e3.png)
User will be asked about cash amount for payment. Once the amount is entered then change is printed on the terminal. 
![image](https://user-images.githubusercontent.com/108750655/209540468-8ee2b963-6e16-4ae7-8512-81adeac46341.png)

### Show total/admin use

This function is only for internal use. Helps administrator to have a balance about sales. Prints all receipts and total sales.
![image](https://user-images.githubusercontent.com/108750655/209544698-f9cf86f5-ae8d-44c3-92f0-87b7af121fda.png)

### Quit

This function terminates the program.
![image](https://user-images.githubusercontent.com/108750655/209545061-1aac7e25-d797-4aeb-a703-a7f2a1a56aec.png)

#   Technology
    
##  Languages used

-   [Python](https://www.python.org/) - high-level, general-purpose programming language
-   [Markdown](https://en.wikipedia.org/wiki/Markdown) - markup language used to write README

##  Software used

- [Font Awesome:](https://fontawesome.com/) - Font Awesome icons were used for social links in terminal display page.

- [Git](https://git-scm.com/) - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

- [GitHub](https://github.com/) - GitHub is used to store the project's code after being pushed from Git.

- [Google Sheets API](https://developers.google.com/sheets/api) - was used to connect with the database made of the spreadsheet.

- [Heroku](https://heroku.com) - online app used to deploy project.

- [VisualStudioCode](https://code.visualstudio.com/) - VSC used to write the app.

- [Text ASCII Art Generator](http://patorjk.com/software/taag/) - used to create app logo in ASCII format.

##  Python libraries/modules

- [gspread](https://docs.gspread.org/) - used for control Google Sheets API by python.

- [OAuthLib](https://pypi.org/project/oauthlib/) - required to manage HTTP request and authenticate to Google Sheets API.

- [PrettyTable](https://pypi.org/project/prettytable/) - python library for easily displaying tabular data in a visually appealing ASCII table format.

- [colorama](https://pypi.org/project/colorama/) - used to color terminal outputs.

- [os](https://docs.python.org/3/library/os.html) - built-in pythod module - used to write clear_terminal function.

- [datetime](https://docs.python.org/3/library/datetime.html) - built-in python module - used to show receipts date and time.


#    Testing
## Manual testing

Details of manual testing can be found in [TESTING.md file](https://github.com/EmanuelMariusNicu/store-management/blob/main/TESTING.md)
