#polymorphism -> overloading-operator overloading
# class Book():
#     def __init__(self,pages):
#         self.pages=pages
#     #magic method
#
#     def __add__(self, other):
#        return self.pages+other.pages
#
#     def __sub__(self, other):
#        return self.pages-other.pages
#
# b=Book(400)
# b1=Book(300)
# print('Total pages in both books :',b+b1)
# print('pages in  both books:',b-b1)

class Marks():
    def __init__(self, s):
        self.s=s
    def __gt__(self, other):
      return self.s>other.s


s1=Marks(100)
s2=Marks(90)
print('student1 have greater marks than student2 : ',s1>s2)


