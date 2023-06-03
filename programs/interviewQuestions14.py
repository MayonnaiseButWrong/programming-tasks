def selectionSort(ins):
    for count in range(len(ins)-1):
        index=count+1
        for i in range(count,len(ins)):
            if ins[index]<=ins[i]:
                index=i
        ins=[ins.pop(index)]+ins
    ins=[ins.pop(-1)]+ins
    return ins

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
    print(selectionSort(l))
