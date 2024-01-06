import tensorflow as tf
import numpy as np

print("hi")

def simultanous(A,B):
    A,B=tf.convert_to_tensor(A,dtype="float32"),tf.transpose(tf.convert_to_tensor(B,dtype="float32"))
    print(B)
    Ainv=tf.linalg.inv(A)
    return tf.multiply(Ainv,B)

def ui():
    l=int(input("number of unknowns: "))
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
print(simultanous(A,B))