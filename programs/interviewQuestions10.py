def sym(*args):
    c=args[0]
    for i in range(1,len(args)):
        a,b,c=c,args[i],[]
        for element in a:
            if not element in b and not element in c:
                for j in range(len(c)):
                    if element<c[j]:
                        c=c[:j]+[element]+c[j:]
                        break
                else:
                    c.append(element)
        for element in b:
            if not element in a and not element in c:
                for j in range(len(c)):
                    if element<c[j]:
                        c=c[:j]+[element]+c[j:]
                        break
                else:
                    c.append(element)
    return c

print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))
        