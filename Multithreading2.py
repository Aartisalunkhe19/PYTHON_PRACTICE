#join
import time
from threading import *
# class MyThread(Thread):
#     def run(self):
#         for i in range(2):
#             print('Child Thread')
#             time.sleep(2)
# t=MyThread()
# t.start()
# #t.join() #it first exexutes Mythread and then main thread
# t.join(2) #it wait for 2 seconds,execyes MyThread and then execute all threads
# for i in range(2):
#     print('Main Thread')

#setting and getting thread Name

# class MyThread(Thread):
#     def run(self):
#         for i in range(2):
#             print('Child Thread')
#             time.sleep(2)
# t=MyThread()
# t.start()
# print('Thread Name : ',t.name)
# t.name='Aarti'
# print('Thread Name ',t.name)
# print('Thread identification number ',t.ident) # the number is change in every execution

#Daemon Thread: Background running thread
# class MyThread(Thread):
#     def run(self):
#         for i in range(2):
#             print('Child Thread')
#             time.sleep(2)
# t=MyThread()
# print('Is Daemon',t.isDaemon())  #False
# t.setDaemon(True) # setting the daemon thread
# print('Is Daemon',t.isDaemon()) #True

# class MyThread(Thread):
#     def run(self):
#         for i in range(2):
#             print('Child Thread')
#             time.sleep(2)
# t=MyThread()
# t.start()
# print('Is Daemon',t.isDaemon())  #False
# t.setDaemon(True) # RuntimeError: cannot set daemon status of active thread
# print('Is Daemon',t.isDaemon()) #False

# class MyThread(Thread):
#     def run(self):
#         for i in range(2):
#             print('Child Thread')
#             time.sleep(2)
# t=MyThread()
# t.start()
# t.start() #RuntimeError: threads can only be started once


#Synchronisation = It executes 1 after another
l=Lock()
def wish(name):
    l.acquire()
    for i in range(2):
        print('Good Evening',name)
        time.sleep(2)
    l.release()
t1=Thread(target=wish,args=('Aarti',))#args are given in tuple
t2=Thread(target=wish,args=('Tanvii',))
t3=Thread(target=wish,args=('Srushti',))
t1.start()
t2.start()
t3.start()
