# class student:
#     def __init__(self):
#         self.name='aaa'
#         self.rollno=1
#
#     def study(self):
#         print('Study in python')
#
# s=student()
# print(s.name)
# print(s.rollno)

#
# class classroom:
#     def __init__(self):
#         self.study='Python'
#         self.time='5.30-7.00'
#
#     def keyboard(self):
#         print('Typing......')
#
#
#     def AC(k):
#         print('cooling...')
#         k.app='Games'
# s=classroom()
# print(s.study)
# print(s.time)
# # print(s.keyboard())
# # print(s.AC())
# s.keyboard()
# s.AC()
# print(s.app)

# class Student:
#     def __init__(self):
#         print('Constructor..')
#
# Student()

#no-argument or zero argument constructor
# class Study:
#     def __init__(self):
#         self.name='AAA'
#         self.marks=88.88
#
# s=Study()
# print('Name :',s.name)
# print('Marks :',s.marks)
# print('--------')
# #Parameterised constructor
#
# class Student:
#     def __init__(self,name,marks,age):
#         self.name=name
#         self.marks=marks
#         self.age=age
#     def info(self):
#         print('Name :',self.name)
#         print('Marks :',self.marks)
#
#     def a(self):
#         print('Age :',self.age)

# s=Student('BB',90)
# print('Name :',s.name)
# print('Marks :',s.marks)
#
# s2=Student('C',87)
# print('Name :',s2.name)
# print('Marks :',s2.marks)

# s=Student('B',89,21)
# s.info()
# print('--------')
# s2=Student('C',90,22)
# s2.info()

class Bank:
    bank_name = 'SBI'  # static variable

    def __init__(self, holder_name, acc_number, balance=1000):
        self.holder_name = holder_name
        self.acc_number = acc_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'You deposited {amount} and your balance is {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance.')
        else:
            self.balance -= amount
            print(f'You withdrew {amount} and your balance is {self.balance}')

    def display(self):
        print(f'Welcome to {self.bank_name}')
        print(f'Account Holder: {self.holder_name}')
        print(f'Account Number: {self.acc_number}')
        print(f'Balance: {self.balance}')






class bank:
    bank_name='SBI'
    name=input('Enter Your Name')
    acc_num = int(input('Enter Account Number: '))

    def __init__(self,balance=1000):
        self.balance=balance
    def deposite(self):
        a=int(input('Enter amount to deposite :'))
        self.balance+=a
        print(f'you deposite {a} and your total balance is {self.balance}')
    def withdraw(self):
        b=int(input('Enter amount to withdraw : '))
        if b<=self.balance:
            self.balance-=b
            print(f'You withdraw {b} and your total balance is {self.balance}')
        else:
            print('Transaction Failed')

d=bank()
print(f'WELCOME TO {d.bank_name} {d.name} your account number is {d.acc_num}')

while True:
    k=input('Select Option : \n1.Deposite amount \n2.withdraw amount')
    if k=='1':
        d.deposite()
    elif k=='2':
        d.withdraw()
    op = input('\nDo you want to perform an operation? (y/n): ')
    if op=='n':
        break


