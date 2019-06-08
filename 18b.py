import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = ["a", "b", "c", "d", "e", "f", "g", "h"]
pat = input("Комірка: ")
if pat[0] not in l or int(pat[1])>8 or int(pat[1])<1 :
    print("Такої нема")
elif ((l.index(pat[0])+1) + int(pat[1]))%2 == 0:
    print("Комірка чорна")
else:
    print("Комірка біла")
printTimeStamp("Денис")
