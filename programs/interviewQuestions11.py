def updateInventory(arr1, arr2):
    for a in range(len(arr2)):
        flag=False
        for b in range(len(arr1)):
            if arr2[a][1]==arr1[b][1]:
                arr1[b][0]+=arr2[a][0]
                flag=True
        if flag==False:
            arr1.append(arr2[b])  
    return arr1
    
curInv=[    #?
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]
newInv=newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

newInv  

#print(updateInventory(curInv, newInv))
print(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], []))