import tkinter as tk  
  

class PassBook(tk.Tk):  
  
    def __init__(self, *args, **kwargs):  
          
        tk.Tk.__init__(self, *args, **kwargs)  
        container = tk.Frame(self)  
        container.pack(side="top", fill="both", expand = True)  
        container.grid_rowconfigure(0, weight=1)  
        container.grid_columnconfigure(0, weight=1)  
  
        self.frames = {}  

        for F in (StartPage, PageOne, PageTwo):  
  
            frame = F(container, self)  
            self.frames[F] = frame  
            frame.grid(row=0, column=0, sticky="nsew")  
  
        self.show_frame(StartPage)  
  
    def show_frame(self, cont):  
  
        frame = self.frames[cont]  
        frame.tkraise()  
  
          
class StartPage(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self,parent)  
        Label1=tk.Label(self,text="Log In",font='display 18').place(x=250,y=50)
        Label2=tk.Label(self,text="User Id ",font='display 18').place(x=80,y=100)
        ent2=tk.Entry(self,font='display 18').place(x=180,y=100)
        Label3=tk.Label(self,text="PassWord ",font='display 18').place(x=60,y=160)
        ent3=tk.Entry(self,font='display 18').place(x=180,y=160)
        Butt=tk.Button(self,text="SUBMIT",font='display 16',command=lambda:controller.show_frame(PageOne)).place(x=250,y=210)

  
class PageOne(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)  
        
        Add_money=tk.Button(self,text="Add Money",bg="#98AFC7",fg="black",width=20,height=4,activebackground="#52595D")
        Add_money.place(x=210,y=70)

        Withdraw_Money=tk.Button(self,text="Withdrow Money",width=20,height=4, bg="#98AFC7",fg="black",activebackground="#52595D",state='disabled')
        Withdraw_Money.place(x=210,y=160)

        Check_Balance=tk.Button(self,text="Check Balance",width=20,height=4,bg="#98AFC7",fg="black",activebackground="#52595D",state="disabled")
        Check_Balance.place(x=210,y=250)
    
class PageTwo(tk.Frame):  
  
    def __init__(self, parent, controller):  
        tk.Frame.__init__(self, parent)  
         
  
app = PassBook()
app.geometry("550x400") 
app.mainloop()  