def Fibonacci(maxdepth,depth,a,b):
    if depth<maxdepth:
        return [a] + Fibonacci(maxdepth, depth+1, b, a+b)
    else:
        return [b]

print(Fibonacci(998, 1, 1, 1))