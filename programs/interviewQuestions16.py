def quickSort(ins):
    if len(ins)<=0:
        return 'NoneType'
    elif len(ins)<=1:
        return ins
    elif len(ins)<=2:
        if ins[0]>ins[-1]:
            return [ins[1]]+[ins[0]]
        else:
            return ins
    else:
        lpointer,rpointer=[],[]
        for i in range(len(ins)-1):
            if ins[i]<=ins[-1]:
                lpointer.append(ins[i])
            else:
                rpointer.append(ins[i])
        lpointer,rpointer=quickSort(lpointer),quickSort(rpointer)
        if lpointer=='NoneType':
            return [ins[-1]]+rpointer
        elif rpointer=='NoneType':
            return lpointer+[ins[-1]]
        else:
            return lpointer+[ins[-1]]+rpointer

import time
from contextlib import contextmanager

import random
l=[]
for i in range(1000000):
    l.append(random.randint(0,1000000))
print(l)

@contextmanager
def timer(label: str):
    start: float = time.perf_counter()
    try:
        yield
    finally:
        end: float = time.perf_counter()
        print(F'{label}: {end - start:.3f} secs')

with timer('Func'):
    print(quickSort(l))
