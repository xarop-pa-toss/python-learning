import csv
import datetime

inventory = {}

def load_inventory(filename):
    # Reads inventory.csv and returns a dictionary {ball_type: quantity}
    with open("csv_files/inventory.csv", "r") as csv_file:
<<<<<<< HEAD
        csv_reader = csv.DictReader(csv_file, fieldnames=None)
        for line in csv_reader:
            print(line)
        csv_file.close()
                    
=======
        csv_reader = csv.DictReader(csv_file, fieldnames=None) 
        for line in csv_reader:
            my_list = []
            my_list.append(line)
        return my_list
    
>>>>>>> 1610f67 (**ignore**)
def save_inventory(filename, inventory):
    # Writes inventory dictionary back to inventory.csv
    with open("csv_files/inventory.csv", "a") as csv_file:
        my_dict = {"ball_type":int("quantity")}
        csv_writer = csv.DictWriter(csv_file, fieldnames=None)
        for line in my_dict:
            csv_writer.writerow(line)
              
def record_sale():
    # Ask user which ball, how many; update inventory and log to sales.csv
    ball_type = input_to_int("What type of ball would you like to buy?\nEnter 1 for Basketballs\nEnter 2 for Bouncy Balls\nEnter 3 for Yoga Balls\nEnter 4 for Tennis Balls\nEnter 5 for Golf Balls")
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
        print("Invalid input")
    amount = input_to_int(f"Enter how many {ball_type} would you like to buy.")
    if amount == int(amount):
        confirmation = input(f"You have purchased {amount} {ball_type}.\nDo you confirm?\nEnter 'Y for Yes or 'N' for No.\n").upper()
        if confirmation == "Y":
            updt_inventory = {ball_type:amount}
            try:
                with open("sales.csv", "a") as csv_file:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=None)
                    for line in updt_inventory:
                        csv_writer.writerow(line)
            except ValueError as e:
                print("Error: ", e)
        elif confirmation == "N":
            return
        else:
            print("Please enter Y or N.")
    else:
        print("Invalid amount. Please input a valid amount in whole numbers.")

def record_purchase():
    # Ask user which ball, how many; update inventory and log to purchases.csv
    pass

def view_inventory():
    # Print out current stock of all balls
    with open("csv_files/inventory.csv", "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            print(line)
    
def monthly_report(year, month):
    # Load sales.csv and show total of each ball_type sold in that month
    pass

def input_to_int(question: str) -> int:
    while True:
        try:
            ball_type = input(f"{question}\nEnter 'q' to exit.\n")
            if ball_type == "q":
                return None
            elif ball_type:
                return int(ball_type)
            else:
                print("Please enter a valid input.")
        except ValueError as e:
            print("Invalid input.", e)
        except ZeroDivisionError as e:
            print("Can't divide by zero.", e)
        except Exception as e:
            print("Error.", e)
          
def month_year():
    now = datetime.datetime.now()
    return now.strftime("%m/%Y")
