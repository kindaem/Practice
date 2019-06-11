import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = {'A':'Newfoundland','B':'Nova Scotia','C':'Prince Edward Island','E':'New Brunswick','G':'Quebec','H':'Quebec', 'J':'Quebec',
'K':'Ontario','L':'Ontario','M':'Ontario','N':'Ontario','P':'Ontario','R':'Manitoba','S':'Saskatchewan','T':'Alberta','V':'British Columbia',
'X':'Nunavut Nortwest Territories','Y':'Yukon'}
while True:
    try:
        code = list(input('Канадський поштовий код: '))
        code[1] = int(code[1])
        code[3] = int(code[3])
        code[5] = int(code[5])
    except ValueError:
        print('Помилочка')
        continue
    if len(code) == 6:
        break
    else:
        print('Помилочка')
        continue
for i in l:
    if i == code[0]:
        print(l.get(i))
    else:
        continue
if code[1] == 0:
    print('Сільска місцевість ')
else:
    print('̳Місто ')
printTimeStamp("Денис")
