def bubbleSort(ins):
    flag=False
    while flag==False:
        flag=True
        for i in range(1,len(ins)):
            if ins[i-1]>ins[i]:
                ins[i],ins[i-1]=ins[i-1],ins[i]
                flag=False
    return ins

def insertionSort(ins):
    for i in range(1,len(ins)):
        for j in range(i):
            if ins[j]>ins[i]:
                ins=ins[:j]+[ins.pop(i)]+ins[j:]
    return ins

def selectionSort(ins):
    for i in range(len(ins)-1):
        index=i+1
        for j in range(i,len(ins)):
            if ins[index]>ins[j]:
                index=j
        ins=ins[:i]+[ins.pop(index)]+ins[i:]
    return ins

def quickSort(ins):
    if len(ins)<=1:
        return ins
    elif len(ins) == 2:
        if ins[0]>ins[1]:
            return [ins[1],ins[0]]
        else:
            return ins
    else:
        l=quickSort([o for o in ins[:-1] if o<=ins[-1]])
        r=quickSort([o for o in ins[:-1] if o>ins[-1]])
        return l+[ins[-1]]+r

def mergeSort(ins):
    if len(ins)<=1:
        return ins
    elif len(ins) == 2:
        if ins[0]>ins[1]:
            return [ins[1],ins[0]]
        else:
            return ins
    else:
        l=ins[:len(ins)//2]
        r=ins[len(ins)//2:]
        l=mergeSort(l)
        r=mergeSort(r)
        out=[]
        while not (len(l)==0 and len(r)==0):
            if len(l)==0:
                out+=r
                break
            elif len(r)==0:
                out+=l
                break
            elif l[0]<r[0]:
                out.append(l.pop(0))
            else:
                out.append(r.pop(0))
        return out


import random
import copy
l=[]
a=1000
for i in range(a):
    l.append(random.randint(0,a))
    #l.append(a-i)

print(mergeSort(copy.deepcopy(l)))
print(quickSort(copy.deepcopy(l)))
print(selectionSort(copy.deepcopy(l)))
print(insertionSort(copy.deepcopy(l)))
print(bubbleSort(copy.deepcopy(l)))

        
