import datetime
import bday_messages

month = 10
day = 20

today = datetime.date.today()
year = today.year
next_birthday = datetime.date(year, month, day)

if next_birthday < today:
    next_birthday = datetime.date(year + 1, month, day)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message())
else:
    print(f"My next birthday is in {days_away} days!")



