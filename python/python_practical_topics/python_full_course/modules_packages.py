

import math
from zoneinfo import reset_tzpath

print(math.pi)

# opt: 3.141592653589793

import random

print(random.randint(1,10))

# its given some random output number from
# 1 to 10


import datetime
now=datetime.datetime.now()
print(now)

# opt: 2024-12-15 20:57:25.394171


# user defined modules:

def add(a,b):
   return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

