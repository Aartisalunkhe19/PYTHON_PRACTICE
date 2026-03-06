import random
#
# # FLOAT
#
# # random.random(): It generates float numbers between 0 and 1
# print("Random float between 0 and 1:")
# for i in range(10):
#     print(random.random())
#
# # random.uniform(a, b): It generates a float number between a and b
# print("\nRandom float between 1 and 2 using uniform():")
# print(random.uniform(1, 2))
#
# # INT
#
# # random.randint(a, b): It generates a random integer between a and b (inclusive)
# print("\nRandom integers between 1 and 10 using randint():")
# for i in range(10):  # Should be range(10) instead of range(1,10) to print 10 numbers
#     print(random.randint(1, 10))
#
# # random.randrange([start], stop, [step]): It returns a randomly selected element from the range
# print("\nRandom integers using randrange():")
# print(random.randrange(10))         # From 0 to 9
# print(random.randrange(10, 21))     # From 10 to 20
# print(random.randrange(10, 21, 5))  # From 10 to 20 with step of 5 (possible values: 10, 15, 20)
#
# # random.choice(): It returns a random element from a non-empty sequence
# name = ['a', 'b', 'c', 'd', 'e']
# print("\nRandom choice from list:")
# print(random.choice(name))


# print('OTP')
# for i in range(4):
#     print()
#     for i in range(4):
#         print(random.randint(0, 9),end=' ')
#


for i in range(10):
    print(random.randrange(0,9),end=" ")