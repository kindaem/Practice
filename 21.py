import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
print("Для яйця з холодильника: ", (67**(2/3)*3.7*1.038**(1/3))/((5.4*10**3)*(4*math.pi/3)**(2/3))*math.log(0.76*((4-100)/(70-100))))
print("Для яйця кімнатної температури: ", (67**(2/3)*3.7*1.038**(1/3))/((5.4*10**3)*(4*math.pi/3)**(2/3))*math.log(0.76*((20-100)/(70-100))))
printTimeStamp("Денис")
