import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = []
for i in range(3):
    l.append(int(input("Number: ")))
l.sort()
print(l)
printTimeStamp("Денис")
