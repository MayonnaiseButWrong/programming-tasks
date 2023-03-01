def longest_substring(x):
    substrings,substring=[],""
    for i in range(len(x)-1):
        current,nexts=x[i],x[i+1]
        if (int(current)%2==0 and not int(nexts)%2==0) or (int(nexts)%2==0 and not int(current)%2==0):
            substring+=nexts
        else:
            substrings.append(substring)
            substring=nexts
    for n in range(len(substrings)-1):
        if len(substrings[n])>len(substrings[n+1]):
            temp=substrings[n]
            substrings[n]=substrings[n+1]
            substrings[n+1]=temp
    print(substrings[-1])
    
longest_substring("225424272163254474441338664823")