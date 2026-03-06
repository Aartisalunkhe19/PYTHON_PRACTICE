#try with multiple except block

#Example1
# try:
#     # print(10/0)
#     # a=[10,20,30]
#     # print(a[5])
#     print(a1)
# except ZeroDivisionError:
#     print('cannot divide by zero')
#
# except IndexError:
#     print('Enter correct index')
#
# except NameError:
#     print('vvariable is not define')



#Example2
# try:
#      print(10/0)
#      a=[10,20,30]
#      print(a[5])
#      print(a1)
# except (ZeroDivisionError,IndexError,NameError):
#     print('Something Broke')

#Example3
#Exception is parent of all the exceptions or errors
# try:
#      # print(10/0)
#      a=[10,20,30]
#      print(a[5])
#      print(a1)
# except Exception as msg:
#     print(msg)

#Default Except Block

# try:
#      print(10/0)
#      a=[10,20,30]
#      print(a[5])
#      print(a1)
# except:
#     print('Something Broke')

#try-except - else block : It is executed when there is no exception inside try
# try:
#      print(10/0)
# except Exception:
#     print('Exception')
# else: print('Rest of code')


#try-except with finally block
# try:
#     print('file open')
#     print('Reading data from file',10/0)
#
# except NameError as msg:
#     print(msg)
#
# finally:
#     print('Finally block')
#     print('File close')



#raise : reating an exception

class mina(Exception):
    def __init__(self,msg):
        super(mina,self).__init__(msg)

class maxa(Exception):
    def __init__(self,msg):
        super(maxa,self).__init__(msg)

a=int(input('Enter age: '))
if a>21 and a<=70:
    print('Congratulations')

elif a>=71:
    raise maxa("Not ELIGIBLE")

else:
    raise mina(' sorry Not eligible ')








