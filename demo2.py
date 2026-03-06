from tkinter import *
def f1():
    print(unamevar.get())
    # headingdata.set(unamevar.get())
    # passdata.set(passvar.get())
    # if uname=='Aarti'and passs==111:
    #     headingdata.set(unamevar.get())
    # else:
    #     print('Login Failed')
    # print(unamevar.set(''))
    # print(passvar.set(''))
root=Tk()
root.title('Login Form')
root.minsize(400,400)
passdata=IntVar()
headingdata=StringVar()

heading=Label(textvariable=headingdata,fg='red',font='Arial 10 bold')
heading1=Label(textvariable=passdata,fg='red',font='Arial 10 bold')

unamevar=StringVar()
passvar=IntVar()

uname1=Label(text='Username : ',fg='black',font='Arial 10 bold')
uname=Entry(textvariable=unamevar,fg='Black',borderwidth=3,font='Italic 10 bold')
pass1=Label(text='Password : ',fg='black',font='Arial 10 bold',pady=20)
passs=Entry(textvariable=passvar,fg='Black',borderwidth=3,font='Italic 10 bold')
btn=Button(text='Submit',fg='Black',borderwidth=3,font='Italic 10 bold',bg='grey',pady=10,height=1,width=4,command=f1)

btn.grid(row=2,column=1)
pass1.grid(row=1,column=1)
passs.grid(row=1,column=2)
uname1.grid(row=0,column=1)
uname.grid(row=0,column=2)
heading.grid(row=3,column=4)
heading1.grid(row=4,column=4)
root.mainloop()