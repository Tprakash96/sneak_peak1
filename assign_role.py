import random;
roles = ['killer','innocent']

print("Enter the number of players...")
personsCount = input()

def genPersons(killerPosition):
    personsRole = []
    for i in range(personsCount):
        if(killerPosition == i):
            personsRole.append("killer")
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

def display(details):
    length = len(details)
    for index in range(length):
        print(details[index])


def main():
    #iteration 1:
    killerPosition = random.randint(0,personsCount-1)
    persons = genPersons(killerPosition)
    display(persons)

    print('\n\n')

    # #iteration 2:
    deathDetails = genDeathDetails(persons,killerPosition)
    display(deathDetails)

    #iteration 3:

main()
