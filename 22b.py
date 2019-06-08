import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Num = input("Частота: ")
num = Num.split("*", 3)
Tic = int(num[0])*int(num[1])**int(num[3])
if Tic < 3*10**9:
    print("Radio waves")
elif Tic >= 3*10**19:
    print("Gamma rays")
elif Tic> 3*10**9 and Tic < 3*10**12:
    print("Microwaves")
elif Tic > 3*10**12 and Tic < 4.3*10*14:
    print("Infrared light")
elif Tic > 4.3*10*14 and Tic < 7.5*10**14:
    print("Visible light")
elif Tic > 7.5*10**14 and Tic < 3*10*17:
    print("Ultraviloet light")
else:
    print("X-ray")
printTimeStamp("Денис")
