import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
for i in range(0, 128):
    print(chr(i), end=' ')
    if (i - 1) % 10 == 0:
        print()

print()
printTimeStamp("Денис")
