import random;

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

print("Enter the number of players...")
n = input()

result = genResult();
#display roles;
for i in range(n):
    print(result[i])