


# data types

# 1. Numeric data types int, flot ,complex

# int

a=20
print("{} is a integer value ".format(a) , type(a))
# output: 20 is integer value , <class 'int'>

# float

a=17.5
print("{} is a float value".format(a),type(a))
# output: 17.5 is a float value , <class 'float'>

# complex
a=5+2j
print("{} is a real number, {} is a imaginary number".format(a.real,a.imag), type(a))
# 5.0 is a real number, 2.0 is a imaginary number , <class 'complex'>

# 2. sequence types string, list tuple

# string

str1='hello'
str2="hello"
str3='''hello'''

print(str1,str2,str3) # opt : hello hello hello

# list

data=['santosh',1,4,7,3+4j]

print(data) # opt: ['santosh',1,4.7, 3+4j]

# tuple

data1=(1,2,3,4,"santosh",3+5j,4.3)

print(data1) # opt: (1,2,3,4,'santosh',(3+5j),4.3)

# 3. Mapping Type

map_data={'name':'santosh','age':'24','dept':'mech'}

print(map_data)  #opt: {'name':'santosh', 'age':'24','dept':'mech'}

# 4. Set Type -> set , frozen set

# set

data_set={1,2,3,4,5,6,7,"santosh",53.24,4+2j}

print(data_set) # opt: {1,2,3,4,5,6,7,'santosh',(4+2j),53.24}

# frozen set

my_dict={}

# create frozenset
data_set1=frozenset([1,2,3])

# use the frozenset as a key in the dictionary
my_dict[data_set1] ="This is a value associated with the frozenset"

print(my_dict[data_set1])
# opt: this is a value associated with the frozenset

# 5. boolean Type

is_valid=True
is_not_valid=False

print(is_valid)           # opt : True
print(is_not_valid)       # opt: False

# 6. Binary Type

# bytes

bin_val=b'hello'

print(bin_val) # opt: b'hello'

# bytearray

bin_array=bytearray(b'santosh')

print(bin_array)   # opt: bytearray(b'santosh')


# memory view

import numpy as np

# from bytes
byte_data=b'hello world'
memory_view=memoryview(byte_data)

print(memory_view)  # opt: <memory at 0x0000027A94C7BD00>


# None Type

x=None

print(x,type(x))  # opt: None <class 'NoneType'>








