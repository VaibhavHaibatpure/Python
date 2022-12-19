from tkinter import *

def txtfile():
    with open ('file path.txt','a') as f:
        name=E1.get()
        #f.write(name)
        path=E2.get()
        #f.write(E2)

file=Tk()
file.geometry('550x250')
file.title('Add Path')

L1=Label(text='Add Path          ' ,font=("Arial", 18)).grid(row=0,column=1)

E1L1=Label(text='  App Name  ',font=("Arial", 18)).grid(row=1,column=0, padx= 7, pady= 8)
E1=Entry(font=("Arial", 18),width='28').grid(row=1,column=1,  padx= 7, pady= 8)

E2L2=Label(text='  Enter Path  ',font=("Arial", 18)).grid(row=2,column=0, padx= 7, pady= 8)
E2=Entry(font=("Arial", 18),width='28').grid(row=2,column=1, padx= 7, pady= 8)

B1= Button(text='Submit',command=txtfile,width='24',height='2').place(x=210,y=150)

file.mainloop()