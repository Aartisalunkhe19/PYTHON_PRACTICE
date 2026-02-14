#overloading->method overloading
# class Test:
#     def m1(self,a=0,b=0,c=0,d=0):
#         print('m1() method calling')
#
# m=Test()
# m.m1()
# m.m1(1,2)
# m.m1('AAA')
# m.m1(True)

#method with var-args arguments
class Test:
    def m1(self,*b):
        print('m1() is calling')

test=Test()
test.m1()
test.m1(True)
test.m1(99)
test.m1(9090)
test.m1('aaa')




