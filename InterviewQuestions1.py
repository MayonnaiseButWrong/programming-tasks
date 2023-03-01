import string
words=0
length=0
flag=False
inputString=str(input('here:'))
for letter in inputString:
    if (letter in string.punctuation or letter == ' '):
        if flag == False:
            print('here',letter)
            words+=1
            flag=True
    else:
        length+=1
        flag=False
if not inputString[-1] in string.punctuation:
    words+=1
print(length/words)