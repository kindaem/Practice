import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Money = int(input("Здача: "))
m5 = Money // 500
m2 = (Money - ((Money // 500)*500))//200
m1 = ((Money - ((Money // 500)*500))-(((Money - ((Money // 500)*500))//200)*200))//100
m50 = (((Money - ((Money // 500)*500))-(((Money - ((Money // 500)*500))//200)*200)) - ((((Money - ((Money // 500)*500))-(((Money - ((Money // 500)*500))//200)*200))//100)*100))//50
m25 = ((((Money - ((Money // 500)*500))-(((Money - ((Money // 500)*500))//200)*200)) - ((((Money - ((Money // 500)*500))-(((Money - ((Money // 500)*500))//200)*200))//100)*100))-(((((Money - ((Money // 500)*500))-(((Money - ((Money // 500)*500))//200)*200)) - ((((Money - ((Money // 500)*500))-(((Money - ((Money // 500)*500))//200)*200))//100)*100))//50)*50))//25
print("Здача: ",m5 , "по 5 грн",m2 , "по 2 грн",m1 , "по 1 грн",m50 , "по 50 коп",m25 , "по 25 коп")
printTimeStamp("Денис")
