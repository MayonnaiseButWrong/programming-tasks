import random
inputList=[]
for i in range(random.randint(0, 10000)):
    inputList.append(random.randint(0,1000))

def check(x):
    n=[]
    if x<2 or x==4:
        return False
    for i in range(2,x//2):
        n.append(i)
    while len(n)>0:
        a=n[0]
        if x%a==0:
                return False
        for y in n:
            if y%a==0:
                n.pop(n.index(y))
    return True            
#print(check(10),check(11))

checkList=list(map(check,inputList))
output=[]
for i in range(len(checkList)):
    if checkList[i]==True:
        output.append(inputList[i])
print(output)