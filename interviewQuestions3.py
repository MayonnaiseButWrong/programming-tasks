import random

def tree(ins):
    if len(ins)>2:
        left,data,right=tree(ins[0:(len(ins)//2)])
        left1,data1,right1=tree(ins[(len(ins)//2)+1:len(ins)])
        print(left1,data1,right1)
        left.append(len(ins)//2)
        right.append(len(ins)-len(ins)//2-1)
        data.append(ins[len(ins)//2])
        return left+left1,data+data1,right+right1
    elif len(ins)==1:
        return [0],ins,[0]
    else:
        if ins[0]<ins[1]:
            return [0,1],ins,[0,0]
        else:
            return [0,1],[ins[1],ins[0]],[0,0]

class BinaryTree:
    def __init__(self,ins):
        self.list=ins
        self.tree=tree(self.list)

inputList=[]
for i in range(random.randint(0, 1000)):
    inputList.append(random.randint(0,1000))
#inputList=[1,3,4,6,8,10]
tree1=BinaryTree(inputList)
print(tree1.tree)