import datetime
from prettytable import PrettyTable as Table
import gspread
from google.oauth2.service_account import Credentials
import helper
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('store-management')

all_products = SHEET.worksheet('products').get_values()
cart = SHEET.worksheet('cart')
receipts = SHEET.worksheet('receipts')
discount_applied = False


def view_products():

    """Function used to display all the products in the store,
       An overview of the prices and stocks of each product """
    table_values = all_products
    table = Table()
    table.field_names = table_values[0]
    table.add_rows(table_values[1:])
    print(table)  

# So any changes to it will be reflected and stored online, not in memory
# Displays just the product names and on which Aisle we can find them
# We can keep adding items to cart, until we type N or n to exit the 
# Buying function and return to main menu


def buy_product():
    """Function to buy/add a product to cart, the cart is stored online"""
    display_items = []
    for val in range(1, len(all_products)):
        display_items.append(all_products[val][0])

    table = Table()
    ailes = []
    for i in range(len(display_items)):
        ailes.append(f"Aisle {i+1}")
    table.field_names = ailes
    table.add_row(display_items)
    print(table)
    add_item_to_cart(display_items) 
    while True:
        user_choice = input("Continue shoping?(Yes/No): ")
        if user_choice.isdigit():
            print("Choose Yes or No:")
        if user_choice.upper() == 'YES':
            helper.reset_screen()
            print(table)
            add_item_to_cart(display_items)
        elif user_choice.upper() == 'NO':
            helper.reset_screen()
            return

# Looks for the item typed against the products in the store
# Prompts the user with the coresponding message
# If the item is available it adds it to the cart/online


def add_item_to_cart(display_items):

    """ Function that handles the logic of buying an item and interaction
        with the DB/google sheet"""
    buy_item = input("Buy/Type(product name): ").title()
    if buy_item not in [x.title() for x in display_items]:
        print("We don't have the product. Choose another product.")
    elif (any(buy_item in f for f in all_products) and
            int(next(f for f in all_products if buy_item in f)[2]) == 0):
        print("Product is out of stock for today.Try again tomorrow.")
    else:
        product = next(f for f in all_products if buy_item in f)
        cart.insert_row([buy_item, float(product[1])])
        print(f"{buy_item} added to your cart.")


def return_item():
    """   Function used to discard/return an item from the cart if we bought 
          to many or changed our minds, you must return an item that you put 
          in the cart in the first place, otherwise it gives an error """
    view_cart()
    item_to_return = input("What item you wish to return: ").title()

    cart_items = cart.get_values()
    is_item_in_cart = any(item_to_return in sublist for sublist in cart_items)
    if not is_item_in_cart:
        print(f"You dont have {item_to_return} in your cart.")
    else:
        for i in range(len(cart_items)):
            if item_to_return in cart_items[i]:
                cart.delete_row(i+1)
                print(f"{item_to_return} has been removed from cart.")
                break


def view_cart():
    """Function to display the products currently in our cart when 
        you want to see if you forgot something"""
    table_values = cart.get_values()
    if len(table_values) == 0:
        print("Your cart is empty, buy something first.")
        return
    table = Table()
    table.field_names = ["Product", "Price"]
    table.add_rows(table_values)
    print(table)
   

def apply_discount(option):

    """Entry function to apply a discount to your cart,
       you can only have a discount applied per cart/purchase
    """
    global discount_applied
    if discount_applied:
        print("A discount has been applied already.")
        return
    if option == 1:
        apply_discount_nr1()
    if option == 2:
        apply_discount_nr2()
    if option == 3:
        apply_discount_nr3() 


# Function also prints a receipt, for internal use, that is stored online
# Receipt/purchase that was done, for accountant, to trac total revenue 
# (functionality to be added later)
# It takes into account the discount when calculating the payment

def pay_print_receipt():

    """ Function to calculate what we have to pay at checkout"""

    global discount_applied
    discount_applied = False
    discount_value = 1
    user_paid = 0
    products = cart.get_values()
    total = 0.0
    for product in products:
        if "Discount" in product:
            discount_value = product[1]
            continue
        total += float(product[1])
    total = round(total, 2) * float(discount_value)
    print(f"You have to pay {total} $")

    while float(user_paid) <= total:
        user_paid = input("Pay cash: ")
    print(f"Your change is: {round(float(user_paid)-total,2)} $")
    print("Have a nice day!")
    
    current_receipt = [f"Receipt {datetime.now()}", total]
    receipts.insert_row(current_receipt)
    cart.delete_rows(1, len(products))


def apply_discount_nr1():

    """ Discount 1 that the store has, if you buy 3 Milk products,
         one is free"""

    global discount_applied
    milk_cartons = 0
    cart_values = cart.get_values()
    for i in range(len(cart_values)):
        if "Milk" in cart_values[i]:
            milk_cartons += 1
            if milk_cartons == 3:
                cart.update_cell(i+1,2,0)
                milk_cartons = 0
    discount_applied = True


def apply_discount_nr2():

    """#Discount 2 that the store has, a 10% off all products, with a voucher
#(that the user suppposedly gives the cashier)"""
    global discount_applied
    discount = ["Discount", 0.9]
    cart.insert_row(discount)
    discount_applied = True
    print("Discount applied.")


def apply_discount_nr3():
    """#discount 3 that the store has, if you buy within one hour of closing time,
        a 30% disccount is applied to the cart"""
    # Closing time is 20:00
    global discount_applied
    now = datetime.now()
    if now.hour >= 19:
        discount = ["Discount", 0.7]
        cart.insert_row(discount)
        discount_applied = True
        print("Discount applied.")
    else: 
        print("Discount cannot be applied, valid after 7PM")