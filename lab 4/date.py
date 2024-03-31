"""
Напишите программу на Python, которая вычитает пять дней из текущей даты.

Напишите программу на Python для печати вчера, сегодня, завтра.

Напишите программу на Python, чтобы отбрасывать микросекунды из даты и времени.

Напишите программу на Python для расчета разницы в двух датах в секундах.
"""
from datetime import date, timedelta, datetime
#1
today = date.today()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)

#2
today = date.today()

print(f'yesterday: {today - timedelta(days = 1)}\ntoday: {today}\ntomorrow: {today + timedelta(days = 1)}')
#3
dt = datetime.now()
dt = dt.replace(microsecond=0)
print(dt, '.00', sep = '')
#4

def difference_in_seconds(date1, date2):
  # Convert dates to timestamps in seconds
  timestamp1 = date1.timestamp()
  timestamp2 = date2.timestamp()

  #
  difference = abs(timestamp1 - timestamp2)

  return difference

# Example for exercise 4
date1 = datetime(2024, 2, 22, 10, 0, 0)
date2 = datetime(2024, 2, 23, 12, 30, 0)

difference = difference_in_seconds(date1, date2)

print(f"The difference between {date1} and {date2} is {difference} seconds.")