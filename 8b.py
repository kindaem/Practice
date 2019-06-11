import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
def precedence(a):
    if a=="+"or a == "-":
        return 1
    elif a=="/"or a == "*":
        return 2
    elif a=="^":
        return 3
    else:
        return -1
if __name__ == "__main__":
    print(precedence(input("Символ: ")))
    printTimeStamp("Доброштан і Глигало")
