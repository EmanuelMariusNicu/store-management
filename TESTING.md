# Manual testing of validation and functionalities

Reasonable amount of manual testing was done to check all inputs and features. <br>


# Main menu
Function used for inputs validation - validate_num_range in utils/utils.py

| What is being tested | Input  | Expected response | Result  |
|---|---|---|---|
|  Please select a number from 1 to 8 to continue | "9" | "asd", "empty"   |Wrong input | Pass
|  Please select a number from 1 to 8 to continue | "1" | Valid input, show view products | Pass
|  Please select a number from 1 to 8 to continue | "2" | Valid input, show buy item | Pass
|  Please select a number from 1 to 8 to continue | "3" | Valid input, show return item | Pass
|  Please select a number from 1 to 8 to continue | "4" | Valid input, show view cart  | Pass
|  Please select a number from 1 to 8 to continue | "5" | Valid input, show apply discounts | Pass
|  Please select a number from 1 to 8 to continue | "6" | Valid input, show pay and print | Pass
|  Please select a number from 1 to 8 to continue | "7" | Valid input, show total receipts| Pass
|  Please select a number from 1 to 8 to continue | "8" | Valid input, quit app/go to main menu | Pass
Please select a number from 1 to 7 to continue | "3" (database is empty)| Valid input, cart is empty/buy first | Pass
Please select a number from 1 to 7 to continue | "4" (database is empty)| Valid input, cart is empty/but first | Pass
Please select a number from 1 to 7 to continue | "5" (database is empty)| Valid input, cart is empty/but first | Pass
Please select a number from 1 to 7 to continue | "6" (database is empty)| Valid input, cart is empty/but first | Pass

# Buy Item function
Buy product from view products list
|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  Buy/Type(product name) | "a"  | Product inexistent/Choose another product/Continue shoping(Yes/No)?| Pass
|  Buy/Type(product name) | "ad"  |Product inexistent/Choose another product/Continue shoping(Yes/No)?| Pass
|  Buy/Type(product name) | "2"  | Product inexistent/Choose another product/Continue shoping(Yes/No)?| Pass
|  Buy/Type(product name) | "234"  |Product inexistent/Choose another product/Continue shoping(Yes/No)?| Pass


# Yes/No question
Function used for inputs validation when buy items.

|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  Continue shoping(Yes/No) | "0"|Wrong input.Choose yes or no: | Pass
|  Continue shoping(Yes/No) |  "y", "Y" | wrong input,Continue shoping(Yes/No)| Pass
|  Continue shoping(Yes/No) |  "n", "N" | wrong input,Continue shoping(Yes/No)| Pass
|  Continue shoping(Yes/No) |  "yes", "no" |valid input, View products| Pass


# Return item function
Return item should match name of product in your cart.
|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  What item do you wish to return? | "6" | Wrong input, you dont have"6"in your cart. | Pass
|  What item do you wish to return?  | "g" | Wrong input, you dont have"g"in your cart  | Pass
| What item do you wish to return? | "eggs" | valid input,"eggs"has been removed from cart | Pass
|  What item do you wish to return? | "6", "database empty"|Wrong input.Your cart is empty,buy something first. | Pass
|  What item do you wish to return?  | "g" , "database empty"| Wrong input.Your cart is empty,buy something first.  | Pass
| What item do you wish to return? | "eggs", "database empty"| Wrong input.Your cart is empty,buy something first. | Pass

# View cart function
View cart products
|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|  View cart | "4" | valid input, show products in cart | Pass
|  View cart | "4", "database empty | valid input, show products in cart | Pass


# Apply discount function
Function used to apply discounts


|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
| Discounts available from 1-4 | "1"  | Valid input, Discount applied| Pass
| Discounts available from 1-4 | "2"  | Valid input, Discount applied  | Pass
| Discounts available from 1-4 | "3"  | Valid input, Discount applied   | Pass
| Discounts available from 1-4 | "4"  | valid input, Back to main menu | Pass
| Discounts available from 1-4 | "1", "database empty"  | Valid input, Your cart is empty,buy something first.| Pass
| Discounts available from 1-4 | "2" , "database empty" | Valid input, Your cart is empty,buy something first. | Pass
| Discounts available from 1-4 | "3" , "database empty" | Valid input, Your cart is empty,buy something first. | Pass
| Discounts available from 1-4 | "4" , "database empty" | valid input, Your cart is empty,buy something first.| Pass


# Pay and print receipts function
Pay for products and receive receipt
|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
| Pay and print receipts | Amount to pay "20" >= products total value  |Valid input, show change amount  | Pass
| Pay and print receipts | Amount to pay, "database empty" |Valid input, Your cart is empty,buy something first | Pass
| Pay and print receipts | Amount to pay,"abc"  |Wrong input,Please insert digits!  | Pass
| Pay and print receipts | Amount to pay, "database empty" |Valid input, Your cart is empty,buy something first | Pass

# Show total receipts
Pay for products and receive receipt
|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
|Show total receipts| "7" |Valid input, show all receipts and sum in a tabel | Pass

# Quit function

|  What is being tested  | Input  | Expected response  | Result
|---|---|---|---|
| Quit | "8"  | Valid input, Quit program  | Pass|
