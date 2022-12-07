
class clg:
    name='DBATU'

class student(clg):
    def __init__(self,studentname,PRN,Branch,Year):
        self.studentname=studentname
        self.PRN=PRN
        self.Branch=Branch
        self.Year=Year
    
    def updateinfo(self,studentname=False,PRN=False,Branch=False,Year=False):
        if studentname:
            self.studentname=studentname
        if PRN:
            self.PRN=PRN
        if Branch:
            self.Branch=Branch
        if Year:
            self.Year=Year

    def info(self):
        a=[self.studentname,self.PRN,self.Branch,self.Year]
        return a

class Teacher(clg):
    def __init__(self,name,salary,branch) -> None:
        self.name=name
        self.salary=salary
        self.branch=branch

    def info(self):
        a=[self.name,self.salary,self.branch]
        return a







a=student('Chutiya',125,'Petro',4)
a.updateinfo(PRN=222,Branch='XXX')
# print(a.info())

# z=Teacher('Vaibhav',50000,'Petro')
val = False
with open ('E:\IT\python\clgstudent.txt','r') as f:
    r=f.readlines()
    
    for i in r:
        k=i.split(' ')
        if int(k[1])!=a.PRN and len(k)>1:
            val = True
        else:
            val = False
with open ('E:\IT\python\clgstudent.txt','a') as f:
    if val:
        for i in a.info():
            f.write(str(i)+' ')
        f.write('\n')
    else:
        print('student is already is here')


# with open ('E:\IT\python\clgteacher.txt','a') as f:
#     for j in z.info():
#         f.write(str(j)+' ')
#     f.write('\n')
    