import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
def calculate_future_date():
    days = int(input("Enter the number of days to add: "))
    current_date = datetime.date.today()
    future_date = current_date + datetime.timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
display_current_datetime()
calculate_future_date()