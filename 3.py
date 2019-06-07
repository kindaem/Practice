import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Letter = input("Літера: ")
if Letter == "a" or Letter =="e" or Letter =="i" or Letter =="o" or Letter =="u":
    print("Введена буква голосна")
elif Letter == "y":
    print("Ця буква може бути голосною або приголосною")
else:
    print("Введена буква приголосна")
printTimeStamp("Денис")
