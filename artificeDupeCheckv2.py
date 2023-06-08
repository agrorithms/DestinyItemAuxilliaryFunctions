import csv
statList  = []
keepFields=['Name','Hash','Id','Tag','Tier','Type','Source','Equippable','Power','Mobility (Base)','Resilience (Base)','Recovery (Base)','Discipline (Base)','Intellect (Base)','Strength (Base)','Total (Base)','Seasonal Mod']
keepFieldsnum = []
startingIndex=keepFields.index('Mobility (Base)')
singleStats = []

with open('eggs.csv', newline='') as csvfile:
    statList  = []
    i = 0
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        singleStats=[]
        if i ==0:
            for index, item in enumerate(row):
                if item in keepFields:
                    keepFieldsnum.append(index)
        else:
            for index, item in enumerate(row):
                if index in keepFieldsnum:
                    if index in range(startingIndex,startingIndex+5):
                        singleStats.append(int(item))
                    else:
                        singleStats.append((item))

            numbers=singleStats.copy()
            statList.append(numbers)


            if statList[-1][-1] == 'artifice':

                for j in range(6):
                    statList[-1][startingIndex+j]= str(int(statList[-1][startingIndex+j])+3)
                    numbers=singleStats.copy()
                    statList.append(numbers)
                    #print(numbers)
                    #print(singleStats)
                  #  print(statList[-j-1])
                statList.pop()
                #    print(str(int(statList[-j-1][startingIndex+j])+3))
                #print(statList)


        i+=1
print(statList)
