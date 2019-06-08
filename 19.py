import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

s=[]
n=0
for i in range(7):
    if input() == "n":
        s.append("off")
    else:
        s.append("on")
    n + 1
print(s)
printTimeStamp("Денис")
