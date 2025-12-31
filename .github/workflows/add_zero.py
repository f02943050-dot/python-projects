# this program wiil add a zero bofor your number and you can type how many zero do you want to add 
# befor your number.


number=input('your number :')

zero=int(input('how many zero do you want?'))

s=len(number)
print(number.zfill(s+zero))
