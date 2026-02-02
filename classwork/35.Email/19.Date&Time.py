from datetime import date

today = date.today()

print(today) # 2025-12-12
print(today.year) # 2025
print(today.month) # 12
print(today.day) # 12
print(today.weekday()) #4
print(today.isoweekday()) #5

print(date(2025, 1, 30)) #2025-01-30

from datetime import date, time

print(date(2025, 12, 12)) #2025-12-12
print(time(11, 45, 25)) #11:45:25

from datetime import date, time, datetime

now = datetime.now()
print(now) #2025-12-12 20:08:04.965100
print(now.year) #2025
print(now.month) #12
print(now.day) #12
print(now.hour) #20
print(now.minute) #8
print(now.second) #4

from datetime import date, time, datetime

now = datetime.now()
print(now.strftime('%Y/%m/%d')) #2025/12/12
print(now.strftime('%d/%m/%Y')) #12/12/2025

print(now.strftime('%d/%m/%Y %H:%M:%S')) #12/12/2025 20:08:05
print(now.strftime('%d/%m/%Y %T:%M:%S %p')) # 12/12/2025 20:08:05:08:05 PM
print(now.strftime('%A %d/%m/%Y %T:%M:%S %p')) #Friday 12/12/2025 20:08:05:08:05 PM
print(now.strftime('%a %d/%m/%Y %T:%M:%S %p')) #Fri 12/12/2025 20:08:05:08:05 PM
print(now.strftime('%a, %d %B %Y %T:%M:%S %p')) #Fri, 12 December 2025 20:08:05:08:05 PM
print(now.strftime('%a, %d %b %Y %T:%M:%S %p')) #Fri, 12 Dec 2025 20:08:05:08:05 PM

from datetime import date, time, datetime, timedelta

today = date.today()
now = datetime.now()

after7 = today + timedelta(days = 7)#2025-12-19

after7m = now + timedelta(minutes = 7) #2025-12-12 20:15:05.372204

after7h = now + timedelta(hours = 7)# 2025-12-13 03:08:05.372204

print(after7, after7m, after7h)
