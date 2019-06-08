import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
print ("{:>0}{:>5}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}".format("",1,2,3,4,5,6,7,8,9,10))
for x in range(1,11):
    print((x), end= '')
    for y in range(1,11):
        print("%4d" % (x*y), end='')
    print()
printTimeStamp("Денис")
