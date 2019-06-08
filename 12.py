import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = []
while True:
    s = int(input("Number: "))
    l.append(s)
    if s == 0:
        break
l.pop()
def midlle(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
print(midlle(l))
printTimeStamp("Денис")
