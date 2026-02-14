
class Addstudent():
    def __init__(self,r,n,c):
        self.r=r
        self.n=n
        self.c=c

class Display():
    def __init__(self):
        self.s={}


    def disp_add(self,r,n,c):
        if r in self.s:
            print('Already Exist')
        else:
            self.s[r] = Addstudent(r,n,c)

    def disp(self):
        for r,stud in self.s.items():
            print(f'Name:{stud.n},RollNo:{stud.r},Coursee:{stud.c}')

    def search(self,r):
        if r in self.s:
            print(f'Name:{n},RollNo:{r},Course{c}')
        else:
            print('Data not present!!')

    def update(self,nn,nc):
        if r in self.s:
            self.s[r].n=nn
            self.s[r].c=nc
            print('Updated Successfully')
        else:
            print('Cannot Update')

    def deletee(self,r):
        if r in self.s:
            del r
            print('Deleted successfully')
        else:
            print('Data not found')

stud=Display()

while True:
    print('====Student Management System====')
    print('1.Add Student')
    print('2.Display student')
    print('3.search Student')
    print('4.Update student')
    print('5.Delete Student')
    print('6.Exit')
    ch=int(input("Enter Your Choice : "))


    if ch==6:
        print('Exit....')
        break

    elif ch==1:
        r=input('Enter RollNo: ')
        n=input('Enter Name: ')
        c=input('Enter Course: ')
        stud.disp_add(r,n,c)

    elif ch==2:
        stud.disp()

    elif ch==3:
        r = input('Enter RollNumber :')
        stud.search(r)
    elif ch==4:
        r=int(input('Enter Roll Number'))
        nn=input('Enter New Name')
        nc=input('Enter New course')
        stud.update(nn,nc)

    elif ch==5:
        r=input('Enter ROll Number')
        stud.deletee(r)
