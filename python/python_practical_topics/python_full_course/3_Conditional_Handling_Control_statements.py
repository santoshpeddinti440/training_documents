

# conditional handling and control statements

# if condition

a=20
b=10

if a>b:
    print("a {} is greater than b {} ".format(a,b))

#opt: a 20 is greater than b 10


# if else condition

a=int(input())

if a%2 == 0:
    print("{} is a even number".format(a))

else:
    print("{} is a odd number".format(a))

# opt: 10 is a even number if given odd number the result is 1 is odd number


# elif ladder

a=20

b=15

if a>b:

    print('a is greater than b')

elif a<b:

    print("b is greater than a")

elif a==b:

    print("a is equal to b")

elif a!=b:

    print("a is not equal to b")

else:
    print("data not sufficient")

# opt: a is greater than b


# Nested if statement

a=24

if a>20:

    if a<26:
        print("you are eligible")
    else:
        print("you are not eligible")
else:
    print("please given valid input data")

# opt: you are eligible


# Control statements

#  break statement

for i in range(1,10):
    if i==5:
        print("loop terminated - ",i)
        break
    print("statement-",i)

# statement- 1
# statement- 2
# statement- 3
# statement- 4
# loop terminated -  5

# continue statement

for i in range(1,10):
    if i==5:
        print("skip the condition - ",i)
        continue
    print("statement - ",i)
    #
    # statement - 1
    # statement - 2
    # statement - 3
    # statement - 4
    # skip the condition - 5
    # statement - 6
    # statement - 7
    # statement - 8
    # statement - 9