import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
years = float(input("Скільки вам років? "))
if years < 1:
    print("Bruh")
elif years < 10.5:
    print(years/10.5, "стільки вам собачих років")
else:
    print(years//10.5 + years % 10.5 / 4, "стільки вам собачих років")
printTimeStamp("Денис")
