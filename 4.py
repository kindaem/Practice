import datetime
from random import randint as r
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = ["the", "a", "one", "some", "any"]
n = ["boy", "girl", "dog", "town", "car"]
v = ["drove", "jumped", "ran", "walked", "skipped"]
p = ["to", "from", "over", "under", "on"]
for i in range(10):
    print(a[r(0, 4)].title() +' '+ n[r(0, 4)] +' '+  v[r(0, 4)] +' '+ p[r(0, 4)] +' '+ a[r(0, 4)] +' '+ n[r(0, 4)]+'.')

printTimeStamp("Доброштан і Глигало")
