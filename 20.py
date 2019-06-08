import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))


for i in range(10):
    print ("  "*(10-i-1) + "*"*(2*i+1))
for i in range(10-1,-1,-1):
    print ('  '*(10-i-1) + "*"*(2*i+1))
