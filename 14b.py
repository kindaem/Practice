import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
V = int(input("Швидкість вітру: "))
T = int(input("Темпераура повітря: "))
WCI = 13.12+0.6215*T-11.37*V**0.16+0.3965*T*V**0.16
print("WCI:", int(WCI))
if V > 4.8 and T<10:
    print("WCI коректний")
printTimeStamp("Денис")
