def getKillerPosition(persons):
    for position in range(len(persons)):
        if persons[position] == 'killer':
            return position

def killPerson(rountNumber,position):
    print("Round : "+rountNumber+" killed person "+position)

arr = ['innocent','innocent','killer','innocent']
killPosition = getKillerPosition(arr)

roundNumber = 0;
for i in range(len(arr)):
    if i != killPosition:
        killPerson(str(roundNumber),str(i))
        roundNumber += 1



