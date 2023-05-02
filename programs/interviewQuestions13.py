import copy
def pairwise(array,num):
    out,checked=0,[]
    for i in range(len(array)):
        temp=copy.deepcopy(array)
        v1=temp.pop(i)
        for v2 in temp:
            if v1+v2==num and not(v1 in checked) and not(v2 in checked):
                j=temp.index(v2)
                out+=i+j
                if j>=i:out+=1
                checked.append(v2)
                break
        checked.append(v1)
    return out


print(pairwise([1,4,2,3,0,5], 7))
print(pairwise([1, 3, 2, 4], 4))
print(pairwise([1, 1, 1], 2))
print(pairwise([0, 0, 0, 0, 1, 1], 1))
print(pairwise([], 100))