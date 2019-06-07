import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
C = int(input("Градуси: "))
K = C + 273,15
F = C*9/5 + 32
print("Кельвіни: ", K)
print("Фаренгейти", C)
printTimeStamp("Денис") 
