import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
n = int(input("Enter an integer (2 or greater): "))
if n < 2:
    print("2 or greater")
factor = 2
prime = []
while factor <= n:
    if n%factor==0:
        prime.append(factor)
        n//factor
    else:
        factor +=1
print(prime)
