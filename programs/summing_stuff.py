def oneThousand(n,N):
    sum=0
    for i in range(n,N):
        sum+=1/(i**3)
    return sum

print(oneThousand(int(input("sum from: ")),int(input("sum to: "))))