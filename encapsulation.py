# class Account():
#     def __init__(self):
#         self.pin=9999
#
# a=Account()
# print(a.pin)
# a.pin=1111
# print(a.pin)
#Here we can easily access and modify data

#Encapsulation
class Account():
    def __init__(self):
        self.__pin=1111

    def getpin(self):
        return self.__pin

    def setpin(self,pin):
        self.__pin=pin

a=Account()
print(a.getpin())
a.setpin(9090)
print(a.getpin())

class employee:
    def __init__(self):
        self.__eid=1
        self.__ename='AAA'
        self.__esalary=25000

    def getemp(self):
        i=int(input('Enter ID : '))
        if i==1:
            return self.__ename,self.__esalary
        else:
            print('Invalid')

    def setemp(self,id,name,salary):
        self.__eid=id
        self.__ename=name
        self.__esalary=salary

e=employee()
print(e.getemp())

class car:
    def __init__(self):
        self.__speed='60km/h'

    def getspeed(self):
        return self.__speed
    def setspeed(self,speed):
        k=int(input('Enter pin :'))
        if k==1919:
            self.__speed=speed
        else:
            print('INVALID')

c=car()
print(c.getspeed())
c.setspeed('70km/h')
print(c.getspeed())
