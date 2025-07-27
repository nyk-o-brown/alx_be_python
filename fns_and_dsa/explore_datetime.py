# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)

def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print("Future Date:", formatted_future)
    except ValueError:
        print("Please enter a valid integer.")

# Script execution
display_current_datetime()
calculate_future_date()
