import datetime 

current_date = datetime.datetime.now()
date1 = datetime.timedelta(days = 1)
Y = current_date - date1
Yesterday = Y.strftime("%Y/%m/%d")
difference = (current_date - Y).total_seconds()

print(difference)