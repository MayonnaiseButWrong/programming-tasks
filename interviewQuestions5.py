import string
ins='this, is an interesting sentence.'
def rev(ins):
    word=''
    other=''
    outputSentence=''
    flag=False
    words=[]
    punctuation=[]
    output=[]
    for letter in ins:
        if letter in string.ascii_letters:
            if flag==True:
                punctuation.append(other)
                other,flag='',False
            word+=letter
        else:
            if not word == '':words.append(word)
            word,flag,other='',True,other+letter
    if not word == '':
                words.append(word) 

    words=words[::-1]
    
    for i in range(len(words)-1):
        output.append(words[i])
        output.append(punctuation[i])  
    if len(words)>len(punctuation):
        output.append(words[i+1])
    
    for j in range(0,len(output)):
        outputSentence+=output[j]
    return outputSentence

print(rev(ins))