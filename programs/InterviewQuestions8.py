import string
def atbash(ins):
    lowers=string.ascii_lowercase
    uppers=string.ascii_uppercase
    reverseLowers=lowers[::-1]
    reverseUppers=uppers[::-1]
    output=''
    for letter in ins:
        if letter in lowers:
            index=lowers.index(letter)
            outputletter=reverseLowers[index]
        elif letter in uppers:
            index=uppers.index(letter)
            outputletter=reverseUppers[index]
        else:
            outputletter=letter
        output+=outputletter
    print(output)

atbash("apple")
atbash("Hello world!")
atbash("Chrismas is the 25th of December")