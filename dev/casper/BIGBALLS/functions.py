import csv
import helpers
from pathlib import Path
from tabulate import tabulate as tab

# Reads a CSV file and returns a list of dictionaries. Each dictionary represents a row, having the column headers (fieldnames) as keys and the cell values as values
def load_csv(filename: str) -> list:
    while True:
        with open(filename, "r+") as csv_file:
            csv_reader = csv.DictReader(csv_file, fieldnames=None) 
            contents_list = []
            for line in csv_reader:
                contents_list.append(line)
            return contents_list
    
# Takes a list of dictionaries (in the format described in load_inventory) and writes to a CSV file.
# Returns True or False depending on if the writing operation succeeded or not.
# ATTENTION: This should only happen once, when the program is shutdown.
def save_csv(filename: str, sale_dict_list: list) -> bool:
    while True:
        if not sale_dict_list:  # If the list is empty, nothing to write
            return False
        with open(filename, "w", newline="") as csv_file:
            # Get fieldnames from the keys of the first dictionary in the list
            csv_writer = csv.DictWriter(csv_file, fieldnames=None, delimiter=",")
            csv_writer.fieldnames = list(sale_dict_list[0].keys())
            csv_writer.writeheader() # Write the header row
            csv_writer.writerows(sale_dict_list)
        return True  # Return True to indicate success

# Takes the name of a ball and a quantity and registers a new sale (a new dictionary) on the sales object (the list read from the CSV).
# This new entry has the ball type, quantity purchased, and timestamp.
# ATTENTION: You can only sell balls that you currently have in stock!
# ATTENTION #2: DO NOT SAVE TO CSV DIRECTLY. Use the lists that were created by reading the CSVs!
def record_sale(saved_purchases: list, saved_inventory: list) -> bool:
    while True:
        ball_type = helpers.input_to_int("What type of ball would you like to sell?\n\nEnter 1 for Basketballs\nEnter 2 for Bouncy Balls\nEnter 3 for Yoga Balls\nEnter 4 for Tennis Balls\nEnter 5 for Golf Balls")
        if ball_type is None:
            return False
        elif ball_type == 1:
            ball_type = "Basketballs"
        elif ball_type == 2:
            ball_type = "Bouncy Balls"
        elif ball_type == 3:
            ball_type = "Yoga Balls"
        elif ball_type == 4:
            ball_type = "Tennis Balls"
        elif ball_type == 5:
            ball_type = "Golf Balls"
        else:
            print("\nPlease enter a valid choice between 1-5.")
            return False
        amount = helpers.input_to_int(f"Enter how many {ball_type} would you like to sell.")
        if amount is None: 
            return False
        elif amount <= 0:
            return print("Please enter a valid amount.")
        confirmation = input(f"\nYou have sold {amount} {ball_type}.\nDo you confirm?\nEnter 'Y' for Yes or 'N' for No.\n").upper()
        if confirmation == "Y":
            try:
            # Update inventory values
                for sale_dict in saved_inventory:
                    saved_quantity = int(sale_dict["Quantity"]) - amount 
                    if sale_dict["Ball Type"] == ball_type:
                        if saved_quantity < 0: 
                            print(f"\nUnable to sell {amount} {ball_type}.\nThis is our current stock for {ball_type}.")
                            print(f"{ball_type}: {sale_dict['Quantity']}")
                            return False
                        sale_dict["Quantity"] = int(saved_quantity)
                        # Insert new line in sales list                                                          
                        saved_purchases.append({"Ball Type": str(ball_type), "Date": str(helpers.date()), "Time": str(helpers.time()), "Quantity": int(amount)})
                        print(f"\nYou have sold {amount} {ball_type}.\nThis is our current stock.")
                        print(tab(saved_inventory, headers="keys", tablefmt="grid"))              
            except ValueError as e:
                print("Error:", e)     
        elif confirmation == "N":
            return False
        else:
            print("Please enter a valid choice.")
              
# Takes in the name of a ball and a quantity and registers a new purchase (a new dictionary) on the purchases object (the list read from the CSV).
# This new entry has the ball type, quantity purchased, and timestamp.
# ATTENTION: You can only have 250 units max of any ball because the Big Balls Inc. warehouse is pretty small. A purchase that exceeds the stock capacity should not be allowed to happen and the user should be informed.
def record_purchase(saved_purchases: list, saved_inventory: list) -> bool:
    while True:
        ball_type = helpers.input_to_int("What type of ball would you like to buy?\nEnter 1 for Basketballs\nEnter 2 for Bouncy Balls\nEnter 3 for Yoga Balls\nEnter 4 for Tennis Balls\nEnter 5 for Golf Balls")
        if ball_type is None:
            return
        elif ball_type == 1:
            ball_type = "Basketballs"
        elif ball_type == 2:
            ball_type = "Bouncy Balls"
        elif ball_type == 3:
            ball_type = "Yoga Balls"
        elif ball_type == 4:
            ball_type = "Tennis Balls"
        elif ball_type == 5:
            ball_type = "Golf Balls"
        else:
            print("\nPlease enter a valid choice between 1-5.")
            return
        amount = helpers.input_to_int(f"Enter how many {ball_type} would you like to purchase.")
        if amount is None: 
            return False
        elif amount <= 0:
            return print("Please enter a valid amount.")
        confirmation = input(f"\nYou have purchased {amount} {ball_type}.\nDo you confirm?\nEnter 'Y' for Yes or 'N' for No.\n").upper()
        if confirmation == "Y":
            # Update inventory values
            try:
                for sale_dict in saved_inventory:
                    saved_quantity = int(sale_dict["Quantity"]) + amount  
                    if sale_dict["Ball Type"] == ball_type:
                        if saved_quantity > 250: 
                            print(f"Unable to sell {amount} {ball_type}\nThis is our current stock for {ball_type}.")
                            print(f"{ball_type}: {sale_dict['Quantity']}\nPlease keep our stock below 250 units.")
                            return False
                        sale_dict["Quantity"] = int(saved_quantity)
                        # Insert new line in purchases list
                        saved_purchases.append({"Ball Type": str(ball_type), "Date": str(helpers.date()), "Time": str(helpers.time()), "Quantity": int(amount)})
                        print(f"\nYou have purchased {amount} {ball_type} for restock")
                        print(f"This is our current stock.\n{tab(saved_inventory, headers='keys', tablefmt='grid')})")
            except ValueError as e:
                print("Error:", e)
            except Exception as e:
                print("Error:", e)   
        elif confirmation == "N":
            return False
        else:
            print("Please enter a valid choice.")
            return False

# Print out current stock of all balls (from the lists).
def view_inventory(saved_inventory: list):
    print("***Big Balls Inc. Current Inventory***")
    for line in saved_inventory:
        print(tab(saved_inventory, headers="keys", tablefmt="grid"))
        return

def monthly_report_sales(saved_purchases):
    while True:
        year = helpers.input_to_int("Enter what year would you like a report on.")
        if year < 2015 or year != helpers.year_now():
            print(f"\nPlease enter a year between 2015-{helpers.year_now()}.")
            return False
        else:
            pass
        month = input(f"\nEnter what month would you like a report on for the year {year}.\nEnter 'q' to exit.\n").lower()
        if month == 'q':
            return False  
        elif month not in helpers.months_str:
            print(f"\nPlease enter a valid month between 01-12.")
            return False
        else:
                try:
                    # iterates through saved_purchases list of dicts and finds correct date
                    for sale_dict in saved_purchases:
                        if sale_dict["Date"] == f"{month}-{year}":
                            print(tab(saved_purchases, headers="keys", tablefmt="grid"))
                            return True
                        elif f"{month}-{year}" not in sale_dict["Date"]:
                            print(f"\n{month}-{year} not found in sales report. This is our current sales.\n{tab(saved_purchases, headers="keys", tablefmt="grid")}")
                            return False
                except ValueError as e:
                    print("Error:", e)
                except Exception as e:
                    print("Error:", e )
                    
def monthly_report_purchases(saved_purchases):
    while True:
        year = helpers.input_to_int("Enter what year would you like a report on.")
        if year < 2015 or year > helpers.year_now():
            print(f"\nPlease enter a year between 2015-{helpers.year_now()}.")
            return False
        else:
            pass
        month = input(f"\nEnter what month would you like a report on for the year {year}.\nEnter 'q' to exit.\n").lower()
        if month == 'q':
            return False  
        elif month not in helpers.months_str:
            print(f"\nPlease enter a valid month between 01-12.")
            return False
        else:
                try:
                    # iterates through saved_purchases list of dicts and finds correct date
                    for sale_dict in saved_purchases:
                        if sale_dict["Date"] == f"{month}-{year}":
                            print(tab(saved_purchases, headers="keys", tablefmt="grid"))
                            return True
                        elif f"{month}-{year}" not in sale_dict["Date"]:
                            print(f"\n{month}-{year} not found in sales report. This is our current sales.\n{tab(saved_purchases, headers="keys", tablefmt="grid")}")
                            return False
                except ValueError as e:
                    print("Error:", e)
                except Exception as e:
                    print("Error:", e )

# Print out the monthly report for the given year-month combo.
def monthly_report(saved_sales, saved_purchases):
    while True:
        print("\n***Big Balls Inc. monthly report menu***")
        try:
            choice = helpers.input_to_int("Would you like a report on Sales or Purchases?\n\nPlease enter 1 for Sales Report or Enter 2 for Purchases Report")
            if choice is None:
                return 
            elif choice == 1:
                monthly_report_sales(saved_sales)
            elif choice == 2:
                monthly_report_purchases(saved_purchases)
            else:
                print("\nPlease enter a valid choice.")
        except ValueError as e:
            print("Error", e)