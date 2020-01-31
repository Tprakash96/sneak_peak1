import random;
import math;

def genRandomNumber(start,end):
    return random.randint(start,end);

def genRole(result): 
    roles = ['killer','innocent']
    while(1):
        role = random.choice(roles)
        if role=="killer" and (role not in result):
            return role;
        elif role=="innocent":
            return role;

def genResult():
    result = []; 
    for i in range(n):
        role = genRole(result)
        result.append(role)
    return result;

def killPerson(personNames,killedPersonList):
    index = random.choice(personNames)
    while(1):
        print(1)
        if index not in killedPersonList:
            return index

print("Enter the number of players...")
n = input()

result = genResult()
# #display roles;
for i in range(n):
    print(result[i])

personNames = []

for i in range(n):
    personNames.append(i)

killPersonList = []

for i in range(n):
    personName = killPerson(personNames,killPersonList)
    killPersonList.append(personName)
    print(killPersonList)


print("vcnfjn")

# for i in range(len(killPersonList)):
#     print("round 1 :" + str(killPersonList[i]))
