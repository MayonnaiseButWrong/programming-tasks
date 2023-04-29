import copy
import time
from contextlib import contextmanager

def generatePerms(ins):
    if len(ins)<=2:
        return [ins,ins[::-1]]
    else:
        out=[]
        for i in range(len(ins)):
            temp=copy.deepcopy(ins)
            temp.pop(i)
            p=generatePerms(temp)
            for j in range(len(p)):
                out.append([ins[i]]+p[j])
        return out

def permAlone(s):
    perms=generatePerms([o for o in s])
    count=0
    for perm in perms:
        for i in range(1,len(perm)):
            if perm[i-1]==perm[i]:
                break
        else:
            count+=1
    return count

@contextmanager
def timer(label: str):
    start: float = time.perf_counter()
    try:
        yield
    finally:
        end: float = time.perf_counter()
        print(F'{label}: {end - start:.3f} secs')

with timer('Func'):
    print(permAlone('abcdefghij'))