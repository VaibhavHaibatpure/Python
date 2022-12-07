import csv
import pandas as pd
with open('E:/nifty.csv','a+') as f:
    ff=csv.writer(f)
    #k=['sr no','name','id','password']
    #ff.writerow(k)
    j=0
    while True:
        j=j+1
        name=input('enter name :')
        id=int(input('enter id :'))
        password=input('enter password :')
        lis=[j,name,id,password]
        ff.writerow(lis)
        z=input('if continue type 1')
        if z!='1':
            break
    #ff=csv.reader(f)
with open('E:/nifty.csv','r') as f1:
    ff1=csv.reader(f1)
    z=[]
    for i in ff1:
        z.append(i)
    z=pd.DataFrame(z)
    print(z)
