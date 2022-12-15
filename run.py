# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('store-management.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('store-management')


def logo():
    print("""

   _____ _                   __  __                              
  / ____| |                 |  \/  |                             
 | (___ | |_ ___  _ __ ___  | \  / | __ _ _ __   __ _  __ _  ___ 
  \___ \| __/ _ \| '__/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \
  ____) | || (_) | | |  __/ | |  | | (_| | | | | (_| | (_| |  __/
 |_____/ \__\___/|_|  \___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|
                                                       __/ |     
                                                      |___/      
    """)


logo()