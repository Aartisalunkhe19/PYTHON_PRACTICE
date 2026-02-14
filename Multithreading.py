from threading import *
import datetime
import time
# print('Current thread Name : ', Thread.name)
# for i in range(10):
#      print("Hello")
#How to create a threading application in python
#1.by using function
# def threds():
#     for i in range(10):
#         print("Hello")
#
# s=Thread(target=threds)
# s.start()
#
# for i in range(10):
#      print("Main Thread")

#2.by extending thread class
# class Mythread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello")
# mt=Mythread()
# mt.start()
#
# for i in range(10):
#      print("Thread")

#without extending thread class
# class mt():
#     def tthred(self):
#         for i in range(10):
#             print("Hello")
# a=mt()
# t=Thread(target=a.tthred())
# t.start()
# for i in range(10):
#      print("Thread")


start_time=time.time()
def square():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in l:
        print(i*i)


def double():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in l:
        print(i*2)

s=square()
time.sleep(2)
print('******')
d=double()
end_time=time.time()
tt=end_time-start_time
print(tt)

