

# creating a function

def my_function():
    print("Hello santosh peddinti")


# calling function

def my_function():

    print("it is a calling function")

my_function()  # opt: it is a calling function


# Arguments

def my_function(first_name):

    print(first_name + " Noted ")

my_function("santosh")
my_function("Aditya")
my_function("Bhaskar")

# opt:

# santosh Noted
# Aditya Noted
# Bhaskar Noted


# parameters or arguments:

def my_function(first_name,last_name):
    print(first_name+" "+last_name)

my_function("santoshkumar","peddinti")

# opt: santoshkumar peddinti

# arbitrary arguments *args

def my_function(*items):
    print("The youngest child is "+items[2])

my_function("Santosh", "Aditya", "bhaskar")

# opt: The youngest child is bhaskar

# keyword arguments:

def my_function(child1,child2,child3):

    print("The youngest child is "+ child3)

my_function(child1="santosh",child2="Aditya",child3="Bhaskar")

# opt: the youngest child is Bhaskar

# arbitrary keyword arguments **kwargs

def my_function(**items):

    print("His last name is "+items["last_name"])

my_function(first_name="santosh",last_name="peddinti")

# opt: Hist last name is peddinti

# default parameter value:

def my_function(country="india"):
    print(" i am from "+ country)

my_function("USA")
my_function("UK")
my_function()
my_function("Brazil")

# input
# i am from USA
# i am from UK
# i am from india
# i am from Brazil


# passing a list as an argument

def my_function(food):
    for x in food:
        print(x)

fruits=["apple","banana","cherry"]

my_function(fruits)

# output:
# apple
# banana
# cherry

# return values

def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# output:

# 15
# 25
# 45


# Recursion

def my_function_recursion(data):
    if(data > 0):
        result=data+my_function_recursion(data-1)
        print(result)
    else:
        result=0
    return result

print("Recursion Example results: ")

my_function_recursion(5)

# opt
# 1
# 3
# 6
# 10
# 15
