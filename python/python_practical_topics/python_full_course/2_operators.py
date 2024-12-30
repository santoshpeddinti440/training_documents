
# 1. Arthematic operators


a=10
b=20

# addition
print(a+b)  # opt: 30

# subtraction
print(b-a)  # opt: 10

# multiplication
print(a*b)  # opt: 200

# division
print(a/b)  # opt: 0.5

#modulus
print(a%b)  # opt: 10

# integer floor
print(a//b) # opt: 0 if the a value is less than b it return 0 other wise
# quotient value given

# power

print(a**b) # opt: 1000000000000000000

# 2. relational operators

a=25
b=15

# less than

print( a<b)   # opt: False

# greater than

print(a>b)    # opt: True

# less than equal

print(a<=b)   # opt: False

# greater than equal

print(a>=b)   # opt: True

# equally

print(a==b)   # opt: False

# not equal

print(a!=b)    # opt: True

# 3. logical operators

a=True
b=False

# and operator

print(a and b)  # opt: False,  in number both are true 2nd number is given output

# or operator

print(a or b)   # opt: True, in number least one true the true number will given

# not operator

print(not a)    # opt: False , its completely opposite of the boolean value

print(not b)    # opt: True,  it completely opposite of the boolean value


# 4. assignment operators

a=20
b=10

# addition

a+=b

print(a)  # opt: 30

# subtraction

a-=b

print(a)   # opt: 20

# multiplication

a*=b

print(a)   # opt: 200

# division

a/=b

print(a)   # opt: 20.0

# modules

a%=b

print(a)    # opt: 0.0

# 5. unary operators

# unary plus:

x=-7
y=+x

print(y)  # opt: -7

# unary minus:

x=5
y=-x

print(y)  # opt: -5

# 6. bitwise operators -> and , or , not

# and operator

a=10    # binary: 1010
b=5     # binary: 0101

# and operator

print(a & b)   # opt: 0   (Binary: 0000)

# or operator

print(a | b)  # opt: 15  (Binary: 1111)

# ^ xor operator

print(a ^ b)  # opt: 15  (Binary: 1111)

# ~ negation operator

print(~a)    # opt: -11 (Depends on system's word size)

# left shift operator

print(a<<2) # opt: 40 (Binary : 101000)

# right shift  operator

print(a>>1) # opt: 5   (Binary: 0101)



# 7. identity operators

x=10
y=10
z=x

print(x is y) # opt: True (both x and y refer to the same integer object)
print(x is z) # opt: True (x and z refer to the same object)

a=[1,2,3]
b=[1,2,3]

print(a is b) # opt: False (a and b are different lists, even if they have the same elements)



# 8. Membership operators

l=[2,3,4,5,6,7,8]

print(2 in l)   # opt: True

print(17 in l)  # opt: False

