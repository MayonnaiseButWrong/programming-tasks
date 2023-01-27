def findComponents(inputString):
    vowels,consonants,spaces = 0,0,0
    for i in range(len(inputString)):
        if inputString[i] == 'a' or inputString[i] == 'e' or inputString[i] == 'i' or inputString[i] == 'o' or inputString[i] == 'u':
            vowels+=1
        elif inputString[i] == ' ' or inputString[i] == '"':
            spaces+=1
        else:
            consonants+=1
    return str(vowels)+' vowels and '+str(consonants)+' consonants'
inString = str(input('Here :'))
print(findComponents(inString))
