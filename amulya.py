import datetime
from datetime import date

now = datetime.datetime.now()
hr = now.hour

def hours_till_valentines():
    today = date.today()
    val_day = date(today.year, 2, 14)
    days_till_val = (val_day - today).days
    hours_till_val = days_till_val * 24
    hours_till_val = hours_till_val - hr
    return hours_till_val
    
wait = datetime.datetime.now().time()
print(str(hours_till_valentines()) + " more hours till 12am on Valentine's Day ):")
