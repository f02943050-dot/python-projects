number=input('your number :')
if '.' in number:
    p=number.split('.')
    d='.'.join([str(int(i))for i in p])
    print(d)
else:
    a=int(number)
    print(a)
