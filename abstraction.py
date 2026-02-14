from abc import *
# class greet(ABC):
#     def wish(self):
#         print('Wishing you ')
    # @abstractmethod
    # def greet(self):
    #     pass

# class Diwali(greet):
#     def greet(self):
#         print('Happy Diwali')
#
# d=Diwali()
# d.wish()
# d.greet()
#
# class Xmas(greet):
#     def greet(self):
#         print('Happy Xmas')
# x=Xmas()
# x.greet()


# class hello(ABC):
#     # @abstractmethod
#     def h(self):
#         print('HELLOO')
#     def name(self):
#         print('Python')
#
# h=hello()
# # h.h()
# h.name()




# class make_payment(ABC):
#     def creditcard(self):
#         print('Payment with credit card')
#
#     def UPI(self):
#         print('Payment with UPI')
#
#     def NetBanking(self):
#         print('Payment with Net banking')
#
# m=make_payment()
# m.creditcard()
# m.NetBanking()
# m.UPI()



class Employee(ABC):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    @abstractmethod
    def calculate_pay(self):
        pass

    def display(self):
        print('Name of emp is: '+self.name)
        print('Id is :'+self.id)

class employeesalary(Employee):
    def calculate_pay(self):

        print('Monthly salary is 25000')

s=employeesalary('AAA','111')
s.display()
s.calculate_pay()


class HourlyEmployee(Employee):
    def calculate_pay(self):
        print('number of hours worked 7 hours/day')
h=HourlyEmployee('xyz','555')
h.calculate_pay()

class commission(Employee):
    def calculate_pay(self):
        print('Commission is 4000')

c=commission('BBB','222')
c.display()
c.calculate_pay()