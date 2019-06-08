import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))

d = float(input("Введіть кількість днів: "))
g = float(input("Введіть кількість годин: "))
h = float(input("Введіть кількість хвилин: "))
s = float(input("Введіть кількість секунд: "))
d1 = 86400
g1 = 3600
h1 = 60
print (int(d*d1 + g*g1 + h*h1+ s))
printTimeStamp("Денис")
