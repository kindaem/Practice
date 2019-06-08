import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
t = int(input("Кількість хвилилн: "))
sms = int(input("Кількість смсок: "))
if t > 200:
    t1 = t - 200
else:
    t1 = 0
if sms > 50:
    sms1 = sms - 50
else:
    sms1 = 0
suma = (35 + t1*0.17 + sms1*0.15)*0.5 + (35 + t1*0.17 + sms1*0.15) + 0.44
print("{:.2f} гривень" .format(suma))
printTimeStamp("Денис")
