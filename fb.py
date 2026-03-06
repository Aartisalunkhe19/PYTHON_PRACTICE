#working with binary file
f=open('/home/lab-04-09/bird.jpeg','rb')
data=f.read(3000)
f2=open('bird2.jpeg','wb')
f2.write(data)
print('img created')