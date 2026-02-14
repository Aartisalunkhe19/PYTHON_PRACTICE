#file handling: read and write data from file is called file handling
#tupes of file handling in python
#character file=.txt,doc,xls
#binary file=img,audio,video,pdf

#f=open('name.txt','w')
#opening modes are:
#w=write, if file not exitst it creates the file
#w+ = write and read
#r=read #default
#r+=read and write
#a=append, if file not exitst it creates the file
# f=open('name1.txt','r') #FileNotFoundError
# f=open('name.txt','w+')
# print('filename :',f.name)
# print('file mode:',f.mode)
# print('Is file closed ',f.closed)
# print(f.readable())
# print(f.writable())

#writing data into file
# f=open('name.txt','w')
# f.write('Aarti\n')
# f.write('Juii\n')
#
# f=open('name.txt','a')
# f.write('Hello\n')
# f.write('Python\n')
#
#
# names=['a','b','c','d']
# f.writelines(names)
# f.close()
#

#reading data from file
# f=open('name.txt','r')
# print(f.read())
# print(f.readline())
# print(f.readlines())
# l=f.readlines()
# for i in l:
#     print(i)

#tell():returns the file pointer location
f=open('name.txt','r')
# print('file pointer location:',f.tell())
# print(f.read(4))
# print('file pointer location:',f.tell())
# print(f.read(4))
# print('file pointer location:',f.tell())
# print(f.read(22))
# print('file pointer location:',f.tell())

#seek(): move file pointer at specific location
# f.seek(1)
# print('file location at:',f.tell())
# print(f.read(4))


f2=open('f2.txt','w+')
f2.write('ccc\n')
f2.write('ddd')
f2=open('f2.txt','r')


f1=open('f1.txt','w+')
f1.write('aaa\n')
f1.write('bbb\n')
f1=open('f1.txt','r')


f3=open('f3.txt','a')
f3.writelines(f1)
f3.writelines(f2)


f3=open('f3.txt','r')
print(f3.read())