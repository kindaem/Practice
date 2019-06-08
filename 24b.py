import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
sound = int(input("Децибели: "))
dc = {130:"Jackhammer",106:"Gas lawnmower",70:"Alarm clock",40:"Quiet room"}
if sound in dc.keys():
    print(dc[sound])
elif sound <40:
    print("Тихіше чим в Quiet room")
elif 70>sound >40:
    print("Між Quiet room і Alarm clock")
elif 106>sound >70:
    print("Між Gas lawnmower і Alarm clock")
elif 130>sound >106:
    print("Між Gas lawnmower і Jackhammer")
else:
    print("Більше Jackhammer")
printTimeStamp("Денис")
