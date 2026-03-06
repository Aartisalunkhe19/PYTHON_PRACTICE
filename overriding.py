#overriding->if the child class have its own method than it is executed otherwise the paent method is executed
class parent():
    def roi(self):
        print('The rate of interest is 5.9%')

class SBI(parent):
    def roi(self):
        print('The roi is 5%')


class HDFC(parent):
    def roi(self):
        print('The roi is 6.5%')


class ICICI(parent):
    def roi(self):
        print('The roi is 7%')

p=parent()
p.roi()

s=SBI()
s.roi()

h=HDFC()
h.roi()

i=ICICI()
i.roi()