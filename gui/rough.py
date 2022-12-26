s='22+3-55*7/2'

count=0
n1=''
k=''
psym=''
total=None
for i in s:
    if i=='+' or i=='-' or i=='*' or i=='/':
        count+=1
        sym=i
        if count>1:
            print(k)
            if i=='+':
                total=int(k)+int(n1)
                k=total
            elif i=='-':
                total=int(k)-int(n1)
                k=total
            elif i=='*':
                total=int(k)*int(n1)
                k=total
            elif i=='-':
                total=int(k)/int(n1)
                k=total

            

        psym=sym
        
    
    if count==1:
        k=n1
        n1=''
    

    if i!='+' or i!='-' or i!='*' or i!='/':
        n1=n1+i

print(total)