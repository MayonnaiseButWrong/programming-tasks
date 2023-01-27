def bubbleSort(inList):
    flag=True
    while flag==True:
        flag=False
        for i in range(len(inList)-1):
            if inList[i]>inList[i+1]:
                temp=inList[i]
                inList[i]=inList[i+1]
                inList[i+1]=temp
                flag=True
    return inList

inputList=[]
for i in range(0,7):
    inputList.append(int(input('Here: ')))
print(bubbleSort(inputList))