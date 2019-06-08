import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
x = ["Дракон","Змія","Кінь","Вівця","Мавпа","Птах","Пес","Свиня","Миша","Бик","Тигр","Заєць"]
y = int(input("Введіть рік: "))
if y >=2000 and y <= 2011:
    print("Рік: ", x[y-2000])
elif y >2011:
    while y >= 2011:
        y-=12
    print("Рік: "+x[y-2000])
elif y <2000:
    while y <= 2000:
        y+=12
    print("Рік: "+x[y-2000])
printTimeStamp("Денис")
