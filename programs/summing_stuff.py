def oneThousand(n,N):
    sum=0
    for i in range(n,N):
        sum+=1/(i**3)
    return sum

def estimate(x):
    return oneThousand(1,x+1)+(2/(x**2)+2/((x-1)**2))/2

print(oneThousand(1,int(input("sum to: "))))
print(estimate(int(input("estimate using: "))))