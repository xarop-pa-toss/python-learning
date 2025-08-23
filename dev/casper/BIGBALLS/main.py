import functions
import helpers

def main_menu():
    # Display menu and loop through options until exit
    while True:
        choice = helpers.input_to_int("Big Balls Inc.\n\nWhat would you like to do?\nEnter 1 to Record a Sale.\nEnter 2 to Record a Purchase.\nEnter 3 to View Current Inventory.\nEnter 4 to View Monthly Report.")
        try: 
            # Needs options for Current Stock report and Monthly Sales report
            if choice is None:
                print("Exiting...")
                return
            elif choice == 1:
                functions.record_sale(saved_sales, saved_inventory)
            elif choice == 2:
                functions.record_purchase(saved_purchases, saved_inventory)
            elif choice == 3:
                functions.view_inventory(saved_inventory)
            elif choice == 4:
                functions.monthly_report(saved_sales, saved_purchases)
        except ValueError as e:
            print("Error: ", e)

if __name__ == '__main__':
    # The following lines get the current directory where Python is running this file.It helps the program know where to look since you might run this on different computers.
    # It also helps if you want to change the folder name or location, you only have to change there reference here
    csv_folder = functions.Path(__file__).parent/"csv_files"
    
    saved_inventory = functions.load_csv(csv_folder/"inventory.csv")
    saved_sales = functions.load_csv(csv_folder/"sales.csv")
    saved_purchases = functions.load_csv(csv_folder/"purchases.csv")
    
    main_menu()
    
    functions.save_csv(csv_folder/"inventory.csv", saved_inventory)
    functions.save_csv(csv_folder/"sales.csv", saved_sales)
    functions.save_csv(csv_folder/"purchases.csv", saved_purchases)
    
    print("finished")