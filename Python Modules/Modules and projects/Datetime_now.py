from datetime import date
import datetime

# print date of today
today=date.today()
print(today)

# give current time
cur_time=datetime.datetime.now().strftime('%H:%M:%S')
print(cur_time)
