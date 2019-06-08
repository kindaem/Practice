import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
print("Ініціалізувати змінну result порожнім рядком")
result = []
print("Оголосити змінну q – число для перетворення")
q = int(input("Число: "))
print("repeat\nОголосити r та присвоїти йому значення остачі від ділення q на 2")
while q > 0:
    r = q % 2
    result.append(str(r))
    q = q//2
print("Звести r до рядкового типу та додати її до початку, \nПоділити націло q на 2 та зберегти результат у q until q не доівнює 0")
print("result")
print(result)
printTimeStamp("Денис")
