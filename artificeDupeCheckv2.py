import csv
statList  = []
keepFields=['Name','Hash','Id','Tag','Tier','Type','Source','Equippable','Power','Mobility (Base)','Resilience (Base)','Recovery (Base)','Discipline (Base)','Intellect (Base)','Strength (Base)','Total (Base)','Seasonal Mod']
keepFieldsnum = []
startingIndex=keepFields.index('Mobility (Base)')
singleStats = []

def createArtificeList(armorcsv):
    ''' using a csv of armor items. function will create a list of armor items, including 6 list elements for each possible use of an artifice armor
    (+ 3 on each stat). To be used later to check if any armor contain a higher stat duplicate'''

    with open(armorcsv, newline='') as armorFile:                               #open csv
        statList  = []
        i = 0
        armorList = csv.reader(armorFile, delimiter=',', quotechar='|')
        for row in armorList:                                                   #loop through armor
            singleStats=[]
            if i ==0:                                                           #use column headers to pull intended fields
                for index, item in enumerate(row):
                    if item in keepFields:
                        keepFieldsnum.append(index)
            else:                                                               #pull intended fields into holder List
                for index, item in enumerate(row):
                    if index in keepFieldsnum:
                        #if index in keepFieldsnum[startingIndex:startingIndex+6]:
                            #singleStats.append(int(item))
                       # else:
                            singleStats.append((item))
                if len(singleStats)>9:
                    numbers=singleStats.copy()                                     #copy holder list so i can append and then alter without effecting original reference
                    statList.append(numbers)


                if statList[-1][-1] == 'artifice':

                    for j in range(6):                                          #if artifice, create 6 elements for each possible stat mximum
                        statList[-1][startingIndex+j]= str(int(statList[-1][startingIndex+j])+3)
                        numbers=singleStats.copy()
                        statList.append(numbers)

                    statList.pop()                                              #remove artifice piece with no +3 stat mod



            i+=1

    return(statList)

def duplicateCheck(artificeList):
    dupeList=[]
    artificeDupePairs = []
    #print(artificeList)
    for checkArmor in artificeList:
        for compareArmor in artificeList:
            if checkArmor[2]!=compareArmor[2] and checkArmor[4] == 'Legendary' and compareArmor[4] == 'Legendary' and checkArmor[7]==compareArmor[7]:

                if checkArmor[5] in ['Helmet','Gauntlets','Chest Armor','Leg Armor'] and checkArmor[5] == compareArmor[5]:
                    #print(checkArmor[startingIndex+1], compareArmor[startingIndex+1]))
                    if int(checkArmor[startingIndex])<=int(compareArmor[startingIndex]) and int(checkArmor[startingIndex+1])<=int(compareArmor[startingIndex+1]) and int(checkArmor[startingIndex+2])<=int(compareArmor[startingIndex+2])and int(checkArmor[startingIndex+3])<=int(compareArmor[startingIndex+3])and int(checkArmor[startingIndex+4])<=int(compareArmor[startingIndex+4])and int(checkArmor[startingIndex+5])<=int(compareArmor[startingIndex+5]):

                        dupeList.append([checkArmor[2],compareArmor[2]])
    for pair in dupeList:
        if pair not in artificeDupePairs:
            artificeDupePairs.append(pair)



    return artificeDupePairs

print(duplicateCheck(createArtificeList('armorList.csv')))
#print(createArtificeList('test1.csv'))

# for row in createArtificeList('armorList.csv'):
#     if len(row) <= 9:
#         print(row)
