maxdepth=997
def pi1(x,n):
    global maxdepth
    if n>=maxdepth:
        return x
    else:
        print(x,(-1 if n%2==0 else 1),(2*n-1))
        return pi1(x+4*((-1 if n%2==0 else 1)/(2*n-1)),n+1)

def pi2():
    x=0
    for n in range(1,100000):
       x+=4*(-1 if n%2==0 else 1)/(2*n-1)
    return x
print(pi2())