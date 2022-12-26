import random
a=['rock','paper','cezzer']
z=input('for rock enter "r" \nfor paper enter "p"\nfor cezzar "c"\nenter:-')
x=random.choice(a)
if x=='rock' and z!='p' :
    print('i have ',x,'\nyou lose')
elif x=='paper' and z!='c' :
    print('i have',x,'\nyou lose')
elif x=='cezzer' and z!='r':
    print('i have',x,'\nyou lose')
else:
    print('i have',x,'\n***you win***')