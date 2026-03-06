import re
# pattern='[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'
# m=input('Enter Number')
# mob=re.fullmatch(pattern,m)
# if mob!=None:
#     print('Valid Number')
# else:
#     print('Invalid Number')

pattern='[A-Z][A-Z][0][1-4][A-Z][A-Z][0-9][0-9][0-9][0-9]'
m=input('Enter Input')
c=re.fullmatch(pattern,m)
if c!=None:
    print('Valid')
else:
    print('Invalid')