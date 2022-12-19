import winapps
 
list_of_app=''
for item in winapps.list_installed():
    list_of_app=list_of_app+str(item)+'\n\n'

application_info=[]
index=['Name','Version','Install_Location','Publisher']
sp3=list_of_app.split('InstalledApplication')
#print(sp3)
for i in sp3:
    #print(i,'\n\n')
    lst=[]
    sp4=list(i.split("'"))
    print(sp4)
    #print(list(sp4[2]))
    lst=sp4
    #print(len(sp4))
    #print(lst[1])
    #   1   3   5   7
    # lst.append(sp4[1])
    # lst.append(sp4[3])
    # lst.append(sp4[5])
    # lst.append(sp4[7])
    for j in range (len(sp4)):
        pass
        #print(sp4[j])
        

    #application_info.append(lst)
    


