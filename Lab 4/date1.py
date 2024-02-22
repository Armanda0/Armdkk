import datetime

current_date = datetime.datetime.now()

current_dates = datetime.timedelta(days=5)
new_date = current_date-current_dates
print(current_date)
print(new_date)