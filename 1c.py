import datetime
import random
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,0,00]
red = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]

s = random.choice(l)
print("Виплатити:", s )
if s in red:
    print("Виплатити: red")
elif s in [0, 00]:
    print("Виплатити: Green")
else:
    print("Виплатити: black")
if s%2 == 0:
    print("Виплатити: Парне")
elif s in [0, 00]:
    pass
else:
    print("Виплатити: Не парне")
if s < 18:
    print("Виплатити: 1 to 18")
else:
    print("Виплатити: 19 to 36")
printTimeStamp("Доброштан і Глигало")
