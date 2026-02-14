class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        print('Area of reactangle: ',self.height*self.width)
    def perimeter(self):
        print('Area of Perimeter: ', 2*(self.height+self.width))

r=Rectangle(10,20)
r.area()
r.perimeter()

print('----------------------')

class Car:
    def __init__(self,model,year,speed=0):
        self.model=model
        self.year=year
        self.speed=speed
    def acc(self):
        print(self.speed+1)
    def brake(self=1):
        if self.speed==0:
            print(0)
        else:
            print(self.speed-1)
    def c_speed(self):
        print(self.speed)

c=Car('TATA',2024,5)
print('Increased speed is :'),c.acc()
print('Decreased speed is :'),c.brake()
print('Current speed is :'),c.c_speed()

# class Bankaccount():
#     def __init__(self,balance=0):
#         self.balance=balance
#     def deposite(self):
#         d=int(input('Enter an amount to deposite'))
#         self.balance+=d
#         print(self.balance)
#     def withdraw(self):
#         if self.balance==0:
#             print('Your account balance is 0')
#         else:
#             w=int(input('Enter amount to withdraw :'))
#             self.balance-=w
#             print(self.balance)
#     def bal(self):
#         print(self.balance)
#
# b=Bankaccount()
# b.deposite()
# b.withdraw()
# b.bal()


class student():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def total_student(self):
        self.id+=1

s1=student('aa',1)
s1.total_student()
