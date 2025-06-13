import datetime as dt

# List of numbered months used in monthly_report. Int wont return 01-09 and error appears
months_str = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

def input_to_int(question: str) -> int:
    while True:
        try:
            ball_type = input(f"\n{question}\nEnter 'q' to exit.\n")
            if ball_type == "q":
                return None
            elif ball_type:
                return int(ball_type)
            else:
                print("\nPlease enter a valid input.")
        except ValueError:
            print("\nInvalid input. Please enter a valid choice.")
        except ZeroDivisionError as e:
            print("Can't divide by zero.", e)
        except Exception as e:
            print("Error.", e)
                  
def date():
    now = dt.datetime.now()
    return now.strftime("%m-%Y")

# Current year for user validation in monthly_report() instead of manually updating it yearly
# This func might be used for future user options
def year_now():
    now = dt.datetime.now()
    year = int(now.strftime("%Y"))
    return year
