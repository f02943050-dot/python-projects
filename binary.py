# this program wil takes a desimal number from the user and converts it to binary whitout using the function(bin)
#LIMITATION:the program works only for numbers up to 225.larger numbers are not suppord yet.


w=int(input('desimal:'))
if w>255:
     print('cant be')
else:
     if w>=128:
        w=w-128
        s='1'
     else:
        s='0'
     if w>=64:
        w=w-64
        f='1'
     else:
        f='0'
     if w>=32:
        w=w-32
        h='1'
     else:
        h='0'
     if w>=16:
        w=w-16
        k='1'
     else:
        k='0'
     if w>=8:
        w=w-8
        m='1'
     else:
        m='0'
     if w>=4:
        w=w-4
        t='1'
     else:
        t='0'
     if w>=2:
        w=w-2
        r='1'
     else:
        r='0'
     if w>=1:
        w=w-1
        d='1'
     else:
        d='0'
x=s+f+h+k+m+t+r+d
print(f'binary:{x}')
