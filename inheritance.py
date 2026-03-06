# #Single Inheritance
# class Animal:
#     def eat(self):
#         print('Eating')
#
# class cat(Animal):
#     def food(self):
#         print('Catfood')
#
# c=cat()
# c.eat()
# c.food()
# print('************************')
# #Multilevel Inheritance
# class car:
#     def tata(self):
#         print('TATA')
#
# class bike(car):
#     def activa(self):
#         print('Activa')
#
# class traveller(bike):
#     def traveller(self):
#         print('Traveller')
#
# t=traveller()
# t.activa()
# t.tata()
# t.traveller()
# print('************************')
# #Hirarchical Inheritance
# class flower:
#     def f(self):
#         print('FLOWER')
#
# class lotus(flower):
#     def l(self):
#         print('Lotus')
#
# class lili(flower):
#     def l2(self):
#         print('lili')
#
# l=lotus()
# l.f()
# l.l()
#
# print('------')
#
# l2=lili()
# l2.f()
# l2.l2()
#
# print('************************')
# #Multiple Inheritance
#
# class parent1:
#     def m1(self):
#         print('parent 1 method 1')
# class parent2:
#     def m2(self):
#         print('parent 1 method 2')
#
# class child(parent1,parent2):pass
#
# c=child()
# c.m1()
# c.m2()

# class parent1:
#     def m1(self):
#         print('parent 1 method 1')
# class parent2:
#     def m1(self):
#         print('parent 1 method 1')
#
# class child(parent1,parent2):pass
# #output = parent 1 method 1 if the method are same then it executes the first class method
# c=child()
# c.m1()
# c.m1()
# while True:
class desset:
    def des(self):
        text=int(input('SELECT DESSERT: 1.ICECREAM \n 2.PESTRY \n 3.BISCUIT \n 4.SWEETS'))
        print(text)


class icecream(desset):
    def type(self):
        a=input('1.scoop----30 /n 2.candy----50 /n 3.cone-----40 ')
        if a==1:
            print('The price of scoop is 30')
        elif a==2:
            print('The price of candy is 50')
        elif a==3:
            print('The price of scoop is 40')
        else:
            print('Try again!!!!!!')
# class pestry(desset):
#     def type1(self):
#         b=input('1.Chocolate pestry----40 \n 2.Truffle pestry----60')
#
# class biscuit(desset):
#     def type2(self):
#         c=input('1.Cream Biscuit----20 \n 2.Oats Biscuit----40')
# class sweets(desset):
#     def type3(self):
#          d=input('1.Gulabjam----20 \n 2.Rasgulla----30 \n 3.Kheer----40')

while True:
    d=icecream()
    d.des()
    d.type()
    a=input('Do you want to repeat y/n : ')
    if d!='y':
        break
# i=icecream()
# i.type()
# p=pestry()
# p.type1()
# b=biscuit()
# b.type2()
# s=sweets()
# s.type3()