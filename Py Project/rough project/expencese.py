import datetime

cash=int(510)

print('add or expence for add enter 1 and for expence enter 2 ')
q=(input('enter here :- '))
'''
try:
    q=int(input('enter here :- '))
except:
    print('you have entered wrong valueg')
'''

a=open("E:\python\python11/expencese.txt","a")
#a.write(cash)

if q =='1':
    w=int(input('enter value :- '))
    cash=cash+w
    r=str(cash)
    a.write('\t\t')
    a.write(r)
    y=str(datetime.datetime.now())
    a.write(y)
    t='\n'
    a.write(t)
elif q=='2':
    w=int(input('enter the value :- '))
    u=input('where do you spend :-')
    r=str(-w)
    a.write(r)
    a.write('\t')
    a.write(u)
    a.write('\t\t')
    y=str(datetime.datetime.now())
    a.write(y)
    a.write('\n')
else:
    print('you have entered wrong value')
a.close()