def mergeSort(ins):
    if len(ins)<2:
        return ins
    elif len(ins)==2:
        if ins[0]>ins[1]:
            return [ins[1]]+[ins[0]]
        else:
            return ins
    else:
        lhalf,rhalf,out,=mergeSort(ins[len(ins)//2:]),mergeSort(ins[:len(ins)//2]),[]
        while not (len(lhalf)==0 and len(rhalf)==0):
            if len(lhalf)==0:
                out+=rhalf
                break
            elif len(rhalf)==0:
                out+=lhalf
                break
            elif lhalf[0]>rhalf[0]:
                out.append(rhalf.pop(0))
            else:
                out.append(lhalf.pop(0))
        return out
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
    print(mergeSort(l))
        
