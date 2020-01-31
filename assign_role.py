import random;
roles = ['killer','innocent']
killerCount = 0
innocentCount = 0

def genRandomPosition(persons):
    return random.choice(persons)

def genRoles(result):    
    while(1):
        role = genRandomPosition(roles)
        if role=="killer" and killerCount < 1:
            killer += 1
            return role
        elif role=="innocent" and innocentCount <= personsCount-1:
            innocentCount += 1
            return role

def genPersons(personsCount):
    result = []; 
    for i in range(personsCount):
        role = genRoles(result)
        result.append(role)
    return result    

def genDeathDetails(persons,killerPosition):
    roundNumber = 0
    details = []
    for i in range(len(persons)):
        if i != killerPosition:
            details.append("Round : "+str(roundNumber)+" killed person "+ str(i))
            roundNumber += 1
    return details

def getKillerPosition(persons):
    for position in range(len(persons)):
        if persons[position] == 'killer':
            return position

def display(details):
    length = len(details)
    for index in range(length):
        print(details[index])

def main():
    #iteration 1:
    persons = genPersons(personsCount)
    display(persons)
    
    #iteration 2:
    killerPosition = getKillerPosition(persons)
    print('\n\n')
    deathDetails = genDeathDetails(persons,killerPosition)
    display(deathDetails)



print("Enter the number of players...")
personsCount = input()

main()
