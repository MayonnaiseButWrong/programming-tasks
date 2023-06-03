def insertionSort(ins):
    for i in range(1,len(ins)):
        count=0
        while count<i:
            if ins[count]>ins[i]:
                ins=ins[:count]+[ins.pop(i)]+ins[count:]
                break
            count+=1
    return ins
            

import time
from contextlib import contextmanager

import random
l=[]
for i in range(1000):
    l.append(random.randint(0,1000))
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
    print(insertionSort(l))
