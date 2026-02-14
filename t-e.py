# print('stmnt1')
# try:
#     print('stmnt2',10/0)
# except ZeroDivisionError:
#     print('Cannot Divide by zero')
#
# print('stmnt3')

# print('stmnt1')
# try:
#     print('HELLO')
#     print('stmnt2',10/0)
# except ZeroDivisionError:
#     print('Cannot Divide by zero')
#
# print('stmnt3')


print('stmnt1')
# try:
#     print('stmnt2',10/0)
#     print('HELLO') # skip
# except ZeroDivisionError:
#     print('Cannot Divide by zero')
#
# print('stmnt3')


# try:
#     n1 = int(input('Enter num1'))
#     n2 = int(input('Enter num2'))
#     div = n1 / n2
#     print(div)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
try:
    num=input('Enter a number: ')
    i=int(num)
    print(i)
except ValueError:
    print('Enter a valid number')


