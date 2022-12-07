from tkinter import *


#       function for prime number
def prime():
    s=In.get()
        
    try:
        for i in range(2,int(s)//2):
            if(int(s)%i)==0:
                lab1=Label(text="NOT PRIME NUMBER",bg='#6495ED',font=('Arial 18'))
                lab1.grid(row=4,column=1)
                break
        else:
            lab1=Label(text="PRIME NUMBER",width=20,bg='#6495ED',font=('Arial 18'))
            lab1.grid(row=4,column=1)
    except:
        pass


#       create screen main widget
screen=Tk()
screen.title("Prime Number Finder")
screen.geometry('400x350')
screen.configure(bg='#686A6C')
screen.resizable(0,0)           #       fix size


#           title for Widget
label=Label(text='Find Prime Or Not',fg='Black',bg='#95B9C7',font=('Arial 15'))
label.grid(row=0,column=1,columnspan=2,pady=10)

lab_lef=Label(text='Enter :',bg='#95B9C7')
lab_lef.grid(column=0,row=2,padx=20)

In=Entry(width=18,font=('Arial 20'))
In.grid(row=2,column=1,pady=20)

button=Button(text="Submit",command=prime)
button.grid(row=3,column=1,pady=20)


#           for my name 😄
lab2=Label(text='By Vaibhav',bg='#686A6C',fg='white',font=('Arial 8'))
lab2.grid(row=5,column=1,pady=80)
screen.mainloop()