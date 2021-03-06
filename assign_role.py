import random;
roles = ['killer','innocent','healer']

print("Enter the number of players...")
personsCount = input()

def genRandomNumber(start,end):
    return random.randint(start,end)

def genPersons(killerPosition,healerPosition):
    personsRole = []
    for i in range(personsCount):
        if(killerPosition == i):
            personsRole.append("killer")
        elif(healerPosition == i):
            personsRole.append("healer")
        else:
            personsRole.append("innocent")
    return personsRole

def genDeathDetails(persons,killerPosition):
    roundNumber = 0
    details = []
    for i in range(len(persons)):
        if i != killerPosition:
            details.append("Round : "+str(roundNumber)+" killed person "+ str(i))
            roundNumber += 1
    return details

def toKillOthers(persons,killerPosition,healerPosition):
    roundCount = 1
    while(1):
        print("\nRound :"+str(roundCount))
        isKillerSuspected = 0
        suspectedCount = [0 for i in range(personsCount)]

        for i in range(len(persons)):
            randomPosition = genRandomNumber(0,len(persons)-1)
            if randomPosition != killerPosition and i == killerPosition:
                print("p"+str(i)+": kills "+"p"+str(randomPosition))
                suspectedCount[randomPosition] += 1
            elif i  == healerPosition and randomPosition != killerPosition:
                print("p"+str(i)+": heals "+"p"+str(randomPosition))
                if suspectedCount[randomPosition] > 0:
                    suspectedCount[randomPosition] -= 1
            elif randomPosition != i:
                suspectedCount[randomPosition] += 1
                print("p"+str(i)+": suspects "+"p"+str(randomPosition))

        for i in range(len(suspectedCount)):
            print("p"+str(i)+": has been suspected "+str(suspectedCount[i]))

        maxSuspected = suspectedCount.index(max(suspectedCount))

        print("The maximum suspected count is "+str(maxSuspected))

        if maxSuspected == killerPosition:
            print "The Killer p"+str(killerPosition)+" has been suspected and killed in round "+str(roundCount)
            break

        elif maxSuspected != killerPosition and maxSuspected >= 1:
            print "The innocent p"+str(maxSuspected)+" has been left with killer in round "+str(roundCount)
            break
        roundCount += 1

def display(details):
    length = len(details)
    for index in range(length):
        print(details[index])

def main():
    mid = (personsCount-1)/2
    #iteration 1:
    killerPosition = genRandomNumber(0,mid)
    healerPosition = genRandomNumber((mid+1),personsCount-1)

    persons = genPersons(killerPosition,healerPosition)
    display(persons)

    print('\n\n')

    # #iteration 2:
    deathDetails = genDeathDetails(persons,killerPosition)
    # display(deathDetails)

    print('\n\n')

    # #iteration 3:
    toKillOthers(persons,killerPosition,healerPosition)
main()
