import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
from winsound import Beep
l = [(440,500), (440,500), (440,500), (349,350), (523,150), (440,500), (349,350), (523,150), (440,1000), (659,500), (659,500),
(659,500), (698,350), (523,150), (415,500), (349,350), (523,150), (440,1000)]
for i in l:
    Beep(i[0], i[1])
printTimeStamp("Доброштан і Глигало")
