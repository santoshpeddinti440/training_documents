

# create a strings

print("Hello") #opt: Hello
print('hello') #opt: hello

# quotes inside quotes:

print("it's alright")
print("hi iam 'santosh'")
print('hi my name is "santosh"')

# opt:
# it's alright
# hi iam 'santosh'
# hi my name is "santosh"

# assign string to a variable

a="Hello"

print(a) # opt: Hello

# Multiline strings

a=""" Lorem ipsum dolor sit amet,
consectetur adipiscing elit,"""

print(a)

# opt:
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,

a='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,'''

print(a)

# opt:
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,

# strings and arrays:

a="Hello, world"
print(a[1])

# opt: e

# looping through a string

for x in "banana":
    print(x)

# opt:
#b
#a
#n
#a
#n
#a

# string length:

a="Hello, world"

print(len(a))

# opt: 12

# check if NOT

str="the best things in life are free"

if "expensive" not in str:
    print("No, 'expensive' is NOT present")
else:
    print("Yes, 'expensive are there in present")

#opt: No, 'expensive' is NOT present

