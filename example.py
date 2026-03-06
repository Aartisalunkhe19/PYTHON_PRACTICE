file=open('file.txt','r')
k=file.read()

a=0
b=0
c=0
for i in k:
    if i.startswith('A'):
        a=a+1
    elif i.startswith('B'):
        b=b+1
    elif i.startswith('C'):
        c=c+1
print('A :',a)
print('B :',b)
print('C :',c)

