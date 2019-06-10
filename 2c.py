import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
date = input("Дата: ")
Date = date.split("-", 3)
year = int(Date[0])
if (year % 400 == 0):
    s = True
elif ((year - ((year // 400)*400))%100 == 0):
    s = False
elif ((year - (((year - (year//400*400))//100)*100))%4 == 0):
    s = True
else:
    s = False
month = int(Date[1])
if month in (1, 3, 5, 7, 8, 10, 12):
    month_l = 31
elif month == 2:
    if s:
        month_l = 29
    else:
        month_l = 28
else:
    month_l = 30
day = int(Date[2])
if day < month_l:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("Наступний день", year,month, day)
for year in (year,day,month):
     if day > month_l:
        break
printTimeStamp("Доброштан і Глигало")
