import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Money = int(input("Скільки грошиків: "))
print("Через рік у вас буде:", Money*0.14 + Money, "через два: ", (Money*0.14 + Money)*0.14 + (Money*0.14 + Money), "і через три роки: ",((Money*0.14 + Money)*0.14 + (Money*0.14 + Money))*0.14 + ((Money*0.14 + Money)*0.14 + (Money*0.14 + Money)))
printTimeStamp("Денис")
