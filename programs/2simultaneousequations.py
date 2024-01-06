def sim(A,B):
    det=1/(A[0][0]*A[1][1]-A[0][1]*A[1][0])
    return det*(B[0]*A[0][0]+B[1]*A[0][1]),det*(B[0]*A[1][0]+B[1]*A[1][1])
    
def ui():
    l=2
    x,y=[],[]
    for n in range(l):
        x.append([])    
    for i in range(l):
        while not len(x[i])==l+1:
            print("write the coefficient in this spot")
            out1=out2=''
            for j in range(l):
                out1+=" A"+str(j)+"x"+str(j)+"+"
            print(out1+" = B")
            for e in x[i]:
                out2+=str(e)+' '
            print(out2)
            x[i].append(int(input("here: ")))
        y.append(x[i].pop())
        print(x)
        print(y)
    return x,y

#A,B=ui()
#print(A,B)
A=[[-13,35],[-35,-13]]
B=[5,0]
print(sim(A,B))