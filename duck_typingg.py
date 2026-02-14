#overloaing->Duck typing

class cat():
    def talk(self):
        print('Meow....Meow')

class dog():
    def talk(self):
        print('Bowww.....Bowww')

class goat():
    def talk(self):
        print('mehhh...mehhh')

def speaking_test(animals):
    for animal in animals:
        animal.talk()

animals=[cat(),dog(),goat()]
speaking_test(animals)


class maths():
    def add(self,*b):
        print(b)

m=maths()
m.add(12+12)
m.add(12+12+90)


class laptop():
    def coding(self):
        print('coading in laptop')

class mobile():
    def coding(self):
        print('coding in mobile')

def developer(device):
    for d in device:
        d.coding()

device=[laptop(),mobile()]
developer(device)