#kinter is GUI used for desktop applications
from tkinter import *

root=Tk()    #Tk() is a class
root.geometry('600x300')
root.title('My first kinter')
root.minsize(300,150)
root.maxsize(700,400)
#Label
heading=Label(text='This is my first component label',fg='red',font='Arial 20 bold',borderwidth=3,
              relief='solid',bg='wheat',padx=50)

msg='''
public static String RevString(String st)
	{
		String	revString="";
		for(int i=st.length()-1;i>=0;i--)
		{
			revString=revString+st.charAt(i);
		}
	return revString;
		
'''
content=Label(text=msg,fg='white',font='Italic 11 bold',borderwidth=3,relief='sunken',bg='grey',padx=50)
heading.pack(fill='x') #fill is used fill the x axis
content.pack(fill='y',anchor='e')
root.mainloop()