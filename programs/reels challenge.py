#input = str(input("enter text here:"))
input = "one hundred and twenty three"
#input = "one hundred and twenty three thousand four hundred and fifty six"

def single_digit_and_teens_and_tens(input):
    if input == "zero":
        return 0
    elif input == "one":
        return 1
    elif input == "two":
        return 2
    elif input == "three":
        return 3
    elif input == "four":
        return 4
    elif input == "five":
        return 5
    elif input == "six":
        return 6
    elif input == "seven":
        return 7
    elif input == "eight":
        return 8
    elif input == "nine":
        return 9
    elif input == "ten":
        return 10
    elif input == "eleven":
        return 11
    elif input == "twelve":
        return 12
    elif input == "thirteen":
        return 13
    elif input == "fourteen":
        return 14
    elif input == "fifteen":
        return 15
    elif input == "sixteen":
        return 16
    elif input == "seventeen":
        return 17
    elif input == "eighteen":
        return 18
    elif input == "nineteen":
        return 19
    elif input == "twenty":
        return 20
    elif input == "thirty":
        return 30
    elif input == "forty":
        return 40
    elif input == "fifty":
        return 50
    elif input == "sixty":
        return 60
    elif input == "seventy":
        return 70
    elif input == "eighty":
        return 80
    elif input == "ninety":
        return 90 
    else:
        return None

def place_values(input):
    if input == "hundred":
        return 100
    elif input == "thousand":
        return 1000
    elif input == "million":
        return 1000000
    elif input == "billion":
        return 1000000000
    elif input == "trillion":
        return 1000000000000
    elif input == "quadrillion":
        return 1000000000000000
    elif input == "quintillion":
        return 1000000000000000000
    elif input == "sextillion":
        return 1000000000000000000000
    elif input == "septillion":
        return 1000000000000000000000000
    elif input == "octillion":
        return 1000000000000000000000000000
    elif input == "nonillion":
        return 1000000000000000000000000000000
    elif input == "decillion":
        return 1000000000000000000000000000000000
    elif input == "undecillion":
        return 1000000000000000000000000000000000000
    elif input == "duodecillion":
        return 1000000000000000000000000000000000000000
    elif input == "tredecillion":
        return 1000000000000000000000000000000000000000000
    elif input == "quattuordecillion":
        return 1000000000000000000000000000000000000000000000
    elif input == "quindecillion":
        return 1000000000000000000000000000000000000000000000000
    elif input == "sexdecillion":
        return 1000000000000000000000000000000000000000000000000000
    elif input == "septendecillion":
        return 1000000000000000000000000000000000000000000000000000000
    elif input == "octodecillion":
        return 1000000000000000000000000000000000000000000000000000000000
    elif input == "novemdecillion":
        return 1000000000000000000000000000000000000000000000000000000000000
    elif input == "vigintillion":
        return 1000000000000000000000000000000000000000000000000000000000000000
    else:
        return None

ins_list = input.split()
print(ins_list)
output_number, cache = 0, 0
for word in ins_list:
    if word == "and":
        continue
    num = single_digit_and_teens_and_tens(word)
    pv = place_values(word)
    if pv is not None:
        output_number += num * pv
    else:
        output_number += num
        
print(output_number)