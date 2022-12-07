import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
z=input('read(r) and write or append (a)\nenter:')
k=['date','invested','current value','day change',"per change",'nifty','day change','nifty per change']

if z=='a':
    with open('E:\my folder/portfolio.csv','a') as f:
        ff=csv.writer(f)
        q=[]        # for input
        for i in k:
            a=input(f'enter {i} :')
            q.append(a)     # insert values
        b=float(q[4])-float(q[7])   # portfolio-nifty change
        bb=round(b,2)               # upto 2 decimal
        q.append(bb)
        print(q)
        ff.writerow(q)      #insert
    
elif z=='r':
    z1=input('if read all type "r"\nread specific date type "d"\nenter:-')
    with open('E:\my folder/portfolio.csv','r') as f:
        fr=csv.reader(f)
        l=[]        # to print
        portfolio=[]    # for chart
        nifty=[]        # for chart
        for i in fr:
            if i :
                l.append(i)     # print
                portfolio.append((i[4]))    # for chart
                nifty.append((i[8]))
        r=pd.DataFrame(l)       # systematic arrangement
        if z1=='r':
            print(r)
            plt.plot(portfolio)     # input values (portfolio %)
            plt.plot(nifty)     # input values (nifty %)
            plt.show()  
        
        # search by specific date
        elif z1=='d':
            z2=input('enter date saperated by "/" (ex. 01/01/2022) \n:-')
            i1=0
            k=['date','invested','current value','day change',"per change",'nifty','day change','nifty per change','nifty vs portfolio']
            for i in (r.loc[:,0]):
                if i==z2:       # finding date row
                    r1=pd.Series(k,index=r.loc[i1,:])
                    zz2=r.loc[i1,:]     # collecting data
                    for i in range (0,len(k)):
                        print(f'{k[i]} = {zz2[i]}')     # column name = values      ex date=00/00/00 , nifty= 1234
                else:
                    i1=i1+1         # increment
else:
    print('wrong input')