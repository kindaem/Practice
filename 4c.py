import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = {1000:20, 2000:35, 5000:85}
s = {1000:0.05, 2000:0.04, 5000:0.02}
trf = int(input("Тариф: "))
mb = int(input("Кількість витрачениx мегабайтів: "))
if (trf==1000) and (mb > 1300):
    print("Тариф: {0} до сплати: {1} + {2}, всього: {3} але якби в взяли б тариф 2000 платили 35 грн".format(trf, l[trf], s[trf]*(mb - trf),s[trf]*(mb - trf) + l[trf]))
elif (trf==2000) and (mb >  3250):
    print("Тариф: {0} до сплати: {1} + {2}, всього: {3} але якби в взяли б тариф 5000 платили 85 грн".format(trf, l[trf], s[trf]*(mb - trf), s[trf]*(mb - trf) + l[trf]))
elif mb <= trf:
    print("Тариф:", trf, "до сплати: ", l[trf], "грн")
else:
    print("Тариф: {0} до сплати: {1} + {2}, всього: {3}" .format(trf, l[trf], s[trf]*(mb - trf),s[trf]*(mb - trf) + l[trf]))
printTimeStamp("Доброштан і Глигало")
