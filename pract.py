def creditcard(num):
    # num=input('Enter a Number:')
    if len(num)>16:
        print('Enter Valid Number')
    elif len(num)<16:
        print('Enter Valid Number')
    else:
        print('**** **** ****', num[12:16])

c=creditcard(num=input('Enter Number'))

