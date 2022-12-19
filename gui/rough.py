import winapps
 
list_of_app=''
for item in winapps.list_installed():
    list_of_app=list_of_app+str(item)

sp1=list_of_app.split("InstalledApplication")

index=['Name','Version','Install_Location','Publisher']
applications=[]

print(sp1)

for i in range(len(sp1)):
    #print(i)
    lst=[]
    if i>0:
        try:
            sp2=sp1[i].split("'")
            #print(sp2)
            #print(sp2[3])
            #   1   3   5   7
            lst.append(sp2[1])
            lst.append(sp2[3])
            lst.append(sp2[5])
            lst.append(sp2[7])
            applications.append(lst)
        except:
            print(sp2)

print(len(sp1))
    #print(sp2)
    #print('\n\n')

for i in applications:
    break
    print(i)
    print()
