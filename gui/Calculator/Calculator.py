
from tkinter import *
from turtle import back, color

calculator=Tk()
calculator.title("Calculator")
calculator.config(background='#3A3B3C')

#================== All Functions   =================================

def add__(a,b):
    return str(int(a)+int(b))

def min__(a,b):
    return (int(a)-int(b))

def mul__(a,b):
    return (int(a)*int(b))

def div__(a,b):
    return (int(a)/int(b))

def number_add_(value):
    temp=screen.get()
    screen.delete(0,END)
    screen.insert(0,temp+value)



def button_(symbol,row,column,value):
    #global z
    #z=''
    symbol=str(symbol)
    value=str(value)
    a=Button(text=symbol,width=10,height=2,borderwidth=5,command=lambda : number_add_(value),bg='#0C090A',font='Display 12',fg='White')
    a.grid(row=row,column=column)

def clear_():
    global z, symbol
    z=None
    symbol=0
    screen.delete(0,END)

def delete_():
    z=screen.get()
    screen.delete(0,END)
    z=z[0:len(z)-1]
    screen.insert(0,z)

def operation_():
    global z
    k=screen.get()
    if symbol=='+':
        ent=str((int(z)+int(k)))
        screen.delete(0,END)
        z=ent

    elif symbol=='-':
        ent=str((int(z)-int(k)))
        screen.delete(0,END)
        z=ent
    
    elif symbol=='*':
        ent=str((int(z)*int(k)))
        screen.delete(0,END)
        z=ent
    
    elif symbol=='/':
        ent=str((int(z)/int(k)))
        screen.delete(0,END)
        z=ent
    

def add_():
    global z, symbol
    #operation('+')
    if z==None:
        z=screen.get()
        screen.delete(0,END)
    else:
        operation_()
    symbol='+'
    print(z,'  ',symbol)

def min_():
    global z, symbol
    if z==None:
        z=screen.get()
        screen.delete(0,END)
    else:
        operation_()
    symbol='-'
    print(z,'  ',symbol)


def mul_():
    global z, symbol
    if z==None:
        z=screen.get()
        screen.delete(0,END)
    else:
        operation_()
    symbol='*'
    print(z,'  ',symbol)


def div_():
    global z, symbol
    if z==None:
        z=screen.get()
        screen.delete(0,END)
    else:
        operation_()
    symbol='/'
    #print(z,'  ',symbol)
    print(z,'  ',symbol)

def equal_():
    global z,symbol
    k=screen.get()
    try:
        if symbol=='+':
            ent=str((int(z)+int(k)))
            z=ent
        elif symbol=='-':
            ent=str((int(z)-int(k)))
            z=ent
        elif symbol=='*':
            ent=str((int(z)*int(k)))
            z=ent
        elif symbol=='/':
            ent=str((int(z)/int(k)))
            z=ent
    except:
        z=0
        pass



    screen.delete(0,END)
    screen.insert(0,z)
    
#=====================================================================================

z=None
symbol=0
result=0
screen=Entry(width=20,borderwidth=3,font='arial 20',bg='#95B9C7')
screen.grid(row=0,column=0,pady=1,columnspan=3)

delete=Button(text='<=Delete=',width=10,height=2,borderwidth=7,command=delete_,bg='#52595D',fg='white')
delete.grid(row=0,column=3)

clear=Button(text='Clear',width=10,height=2,command=clear_,borderwidth=7,bg='#52595D',fg='white')
clear.grid(row=4,column=0)

divide=Button(text='/',width=10,height=2,command=div_,borderwidth=7,bg='#52595D',fg='white')
divide.grid(row=1,column=3)

multiple=Button(text='x',width=10,height=2,command=mul_,borderwidth=7,bg='#52595D',fg='white')
multiple.grid(row=2,column=3)

minus=Button(text='-',width=10,height=2,command=min_,borderwidth=7,bg='#52595D',fg='white')
minus.grid(row=3,column=3)

add=Button(text='+',width=10,height=2,command=add_,borderwidth=7,bg='#52595D',fg='white')
add.grid(row=4,column=3)

equal=Button(text='=',width=10,height=2,command=equal_,borderwidth=7,bg='#52595D',fg='white')
equal.grid(row=4,column=2)

clear=Button(text='C',width=10,height=2,command=clear_,borderwidth=7,bg='#52595D',fg='white')
clear.grid()

button_(7,1,0,7)
button_(8,1,1,8)
button_(9,1,2,9)
button_(4,2,0,4)
button_(5,2,1,5)
button_(6,2,2,6)
button_(1,3,0,1)
button_(2,3,1,2)
button_(3,3,2,3)
button_(0,4,1,0)
#button_('.',4,0,'.')
b=Button(text='.',width=10,height=2,borderwidth=5,state=DISABLED,bg='#0C090A',font='Display 12',fg='White')
b.grid(row=4,column=0)
print(z)


calculator.mainloop()