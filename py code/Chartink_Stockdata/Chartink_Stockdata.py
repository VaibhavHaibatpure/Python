'''
Get data from Chartink Website :
        Open a stock price chart 
        Select 'Inspect' option  (It opens HTML code source)
        In Elements section search 'oridinal_height' which contains the stock price data 
        copy the data and past it into txt file
'''
a=input('Enter txt file path :')
b=input('enter txt file name :')
z=''
if '.txt' in a:
    z=a
elif '.txt' in b:
    z=a+'\\'+b
elif '.txt' not in b:
    b+='.txt'
    z=a+'\\'+b
else:
    print('Somthing wrong')
print(z)
# "F:\\OFSS.txt"
beesdata=[]
with open(z,'r') as file:
    #print(file.read())
    z=file.read()
    #print(z)
    lst=z.split(";")
    #print(lst)
    '''
    temp[755]="207.49,207.49,203.65,204.44,-0.18,05-12-22,1627546";
    temp[754]="207.49,207.49,203.90,204.81,-0.36,02-12-22,2370387";
    '''

    for i in lst:
        new_lst1=i.split('=')       # [temp[755] ,"207.49,207.49,203.65,204.44,-0.18,05-12-22,1627546"]
        try:                            #   0               1
            #print(new_lst1[1])          # removing temp[...]  
            new_lst2=new_lst1[1].split(',')
            #print(new_lst2)             #['"126.69', '126.69', '125.85', '126.44', '-0.13', '22-11-19', '367760"']
            beesdata.append(new_lst2)
        except:
            #print('ended...\n')
            pass

#print(beesdata)

    #   Open    High    Low     Close   %Change     Date    Vol
avg=0
count=0
for i in beesdata:
    avg+=(float(i[3]))
    #print(i)
    count+=1
print(count)
print('Average Price is :',avg/count)
