# your computer will chose a number randomly and you should guess it.
# the number is between the 1 to 10.


import random
n=random.randint(0,10)
f='no'

while f=="no" :
    a=int(input('enter your guess:'))
    if a>n:
        print('<')
    else:
        if a<n:
            print('>')
        else:
            print('correct')
            f='yes'
print('thank you')
