#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = number % 10
print(f"Last digit of {number} is {d}", end = " ")
if d > 5:
    print("and is greater than 5")
elif d == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
