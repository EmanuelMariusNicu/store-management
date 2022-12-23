# Write your code to expect a terminal of 80 characters wide and 24 rows high

import storeService as store
import helper


def logo():
    print("""

   _____ _                   __  __                              
  / ____| |                 |  \/  |                             
 | (___ | |_ ___  _ __ ___  | \  / | __ _ _ __   __ _  __ _  ___ 
  \___ \| __/ _ \| '__/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _  
  ____) | || (_) | | |  __/ | |  | | (_| | | | | (_| | (_| |  __/
 |_____/ \__\___/|_|  \___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|
                                                       __/ |     
                                                      |___/      
""")


logo()


def menu():
    print("""
     1. View Products
     2. Buy Item
     3. Return Item
     4. View Cart
     5. Apply Discount
     6. Pay and Print Receipt
     7. Quit
     """)


def discount_menu():
    """ Discount prices that apply"""
    print("""
     1. 3 for price of 2 on Milk
     2. 10% off on all products
     3. 30% off one hour before closing time(8PM)
     4. Back to menu
     """)


def display_menu():
    while True:
        menu()
        user_choice = input("Select a choice: ")

        # reset screen
        helper.reset_screen()

        if not user_choice.isdigit() or int(user_choice) not in range(1,8):
            print("Please select a valid option number from 1..7")

        if user_choice == "1":
            store.view_products()
        elif user_choice == "2":
            store.buy_product()
        elif user_choice == "3":
            store.return_item()
        elif user_choice == "4":
            store.view_cart()
        elif user_choice == "5":
            display_discount_menu()
        elif user_choice == "6":
            store.pay_print_receipt()
        elif user_choice == "7":
            break


def display_discount_menu():
    while True:
        discount_menu()
        user_choice = input("Select a choice: ")

        # reset screen
        helper.reset_screen()

        if not user_choice.isdigit() or not int(user_choice) in range(1,5):
            print("Please select a valid option number from 1-5")

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