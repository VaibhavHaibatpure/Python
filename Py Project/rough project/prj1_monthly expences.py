month=[]
expence=[]

i=1
while i>0:
    a=input('enter the month :')
    b=int(input('enter the expence :'))
    month.append(a)
    expence.append(b)
    print('if you want to continue plz enter 1')
    k=input()
    if k=='1':
        continue
    else :
        break
dic={}
print(month)
print(expence)
#while i<=len(month):
dic={month[i]:expence[i] for i in range (0,len(month))}

print(dic)