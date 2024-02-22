import datetime
current_date = datetime.datetime.now()
current_dates = datetime.timedelta(days=1)
Today=current_date.strftime("%Y/%m/%d")
T =current_date+current_dates
Y=current_date-current_dates
Tomorrow=T.strftime("%Y/%m/%d")
Yesterday=Y.strftime("%Y/%m/%d")
print(Yesterday)
print(Today)
print(Tomorrow)