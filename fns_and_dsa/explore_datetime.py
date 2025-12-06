from datetime import datetime, date, time, timedelta


def display_current_datetime():
    current_date = datetime.now()
    current_date_and_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f'current_date_and_time:  {current_date_and_time}')

    num_of_days = int(input("Enter the number of days to add to the current date: "))
    def calculate_future_date():
        now = datetime.now()
        future_date = now + timedelta(days=num_of_days)
        print(f'Future date after adding {num_of_days} days: {future_date.strftime("%Y-%m-%d")}')
    calculate_future_date()
display_current_datetime()