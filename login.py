from tkinter import *

def f1():
     if uname.get()=='Aarti' and passs.get()=='111':
         headingdata.set('Login Successful')
     else:
         headingdata1.set('Login Failed')
root=Tk()
root.title('Login Form')
root.minsize(400,400)
unamevar=StringVar()
headingdata=StringVar()
headingdata1=StringVar()
heading1=Label(textvariable=headingdata1,fg='black',bg='Red',font='Arial 10 bold')
heading=Label(textvariable=headingdata,fg='black',bg='Green',font='Arial 10 bold')
uname1=Label(text='Username : ',fg='black',font='Arial 10 bold')
uname=Entry(textvariable=unamevar,fg='Black',borderwidth=3,font='Italic 10 bold')

pass1=Label(text='Password : ',fg='black',font='Arial 10 bold',pady=20)
passs=Entry(fg='Black',borderwidth=3,font='Italic 10 bold')

btn=Button(text='Submit',fg='Black',borderwidth=3,font='Italic 10 bold',bg='grey',pady=10,height=1,width=4,command=f1)

btn.grid(row=2,column=1)
pass1.grid(row=1,column=1)
passs.grid(row=1,column=2)
uname1.grid(row=0,column=1)
uname.grid(row=0,column=2)
heading.grid(row=3,column=1)
heading1.grid(row=3,column=1)
root.mainloop()