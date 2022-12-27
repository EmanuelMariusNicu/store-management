# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time
import colorama
from colorama import Fore
import storeService as store
import helper

# Function to display ASCI text about app logo


def logo():
    print(Fore.GREEN + """
 
   _____ _                   __  __                                                   _    
  / ____| |                 |  \/  |                                                 | |   
 | (___ | |_ ___  _ __ ___  | \  / | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_  
  \___ \| __/ _ \| '__/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __| 
  ____) | || (_) | | |  __/ | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_  
 |_____/ \__\___/|_|  \___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__| 
                                                       __/ |                               
                                                      |___/                                
                         
""")


print(Fore.BLUE + """Welcome to our Store Management App shop cart.
Use the menu below to continue:""")


# Menu function


def menu():
    print(Fore.CYAN + """
     1. View Products
     2. Buy Item
     3. Return Item
     4. View Cart
     5. Apply Discount
     6. Pay and print receipts
     7. Show total receipts(admin use)
     8. Quit
     """)
# Discount function that applies for all products


def discount_menu():
    """ Discount prices that apply"""
    print("Discount offers in our shop")
    print("""
     1. 3 for price of 2 on milk
     2. 10% off on all products
     3. 30% off one hour before closing time(8PM)
     4. Back to menu
     """)
# Menu function for choices from 1 to 8


def display_menu():
    logo()
    time.sleep(6)
    helper.reset_screen()
    while True:
        menu()
        user_choice = input("Select a choice from 1-8 to continue: ")

        # reset screen
        helper.reset_screen()

        if not user_choice.isdigit() or int(user_choice) not in range(1, 8):
            print("Please select a valid option number from 1-8")

        if user_choice == "1":              # Menu view products
            store.view_products()
        elif user_choice == "2":            # Menu buy project
            store.buy_product()
        elif user_choice == "3":            # Menu return item
            store.return_item()
        elif user_choice == "4":            # Menu view cart
            store.view_cart()
        elif user_choice == "5":            # Menu discounts
            display_discount_menu()
        elif user_choice == "6":            # Menu pay and print receipt
            store.pay_print_receipt()
        elif user_choice == "7":            # Menu administrator total sales
            store.show_total_sale()
        elif user_choice == "8":            # Menu quit choice
            exit_print_message()
            break
# Messages printed in terminal when exit app


def exit_print_message():
    print("Thank you for using Store Management App.")
    print("This app was developed by Marius Emanuel Nicusor.")
    print("Finished..")
# Function discount menu inside discount that applies for products


def display_discount_menu():
    while True:
        discount_menu()
        user_choice = input("Select a choice from above: ")

        # reset screen
        helper.reset_screen()

        if not user_choice.isdigit() or not int(user_choice) in range(1, 5):
            print("Please select a valid option number from 1-4")

        if user_choice == "1":
            store.apply_discount(1)
            break
        elif user_choice == "2":
            store.apply_discount(2)
            break
        elif user_choice == "3":
            store.apply_discount(3)
            break
        elif user_choice == "4":
            break


display_menu()
