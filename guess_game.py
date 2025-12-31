# your computer will chose a number randomly and you should guess it.


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
