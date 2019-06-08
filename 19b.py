import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Marks = {"A+":">4.0","A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"F":0}
Mark = input("Оцінка: ")
if Mark in Marks.keys():
    print("Оціночка: "+str(Marks[Mark]))
else:
    print("Нема такої")
printTimeStamp("Денис")
