

# 1. enter your name 100 times
str=input("Enter your name here: ")

for i in range(100):
    print(str)

# 2. even or odd number

num=int(input("Enter the number: "))

if num%2 == 0:
    print(f"the number is even: {num}")
else:
    print(f"the number is odd: {num}")

# 3. write a program to print 7 th table

num=int(input("Enter the number: "))

def seven_table(value):
    for i in range(1,11):

        print(value, "x", i ,"=",value*i)

seven_table(num)

# opt:

# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# 4. python program to find max and minimum

a=535
b=53

print("maximum number is: ",max(a,b)) #opt : maximum number is  90

print("minimum number is: ",min(a,b)) #opt: minimum number is   3

# 5. find the maximum number

list=[535,24,224,66,78,686,46,96,56,32,10,5]

print("the maximum number: ",max(list))

# opt: the maximum number: 686

# list operations

# create the list

list_items=[1,2,55,33,67,54,"santosh","peddinti",166.35]

# access the list items

for str in range(len(list_items)):
    print(list_items[str])


# opt:
#
# 1
# 2
# 55
# 33
# 67
# 54
# santosh
# peddinti
# 166.35

# change the list items

list_items=[1,2,55,33,67,54,"santosh","peddinti",166.35]

list_items[6]="srinu"

print(list_items)

#opt: [1, 2, 55, 33, 67, 54, 'srinu', 'peddinti', 166.35]

# replace the list items

list_items=[1,2,55,33,67,54,"santosh","peddinti",166.35]

list_items[6]="sekhar"
list_items[7]="chatla"

print(list_items)

# opt: [1, 2, 55, 33, 67, 54, 'sekhar', 'chatla', 166.35]


# append the values into the list


list_items=[1,2,55,33,67,54,"santosh","peddinti",166.35]

list_items.append("mahesh")
list_items.append("swarna")
list_items.append("vizag")

print(list_items)

# opt: [1, 2, 55, 33, 67, 54, 'santosh', 'peddinti', 166.35, 'mahesh', 'swarna', 'vizag']

# insert the new items into the list

list_items=[1,2,54,"santosh","peddinti",166.35]

list_items.insert(1,"manibabu")
list_items.insert(5,"gopinadh")

print(list_items)

#opt: [1, 'manibabu', 2, 54, 'santosh', 'gopinadh', 'peddinti', 166.35]


# extend the items in the list

list_items=[1,2,54,"santosh","peddinti",166.35]

list_items.extend([535])
list_items.extend([1535])

print(list_items)

# opt:

# [1, 2, 54, 'santosh', 'peddinti', 166.35, 535, 1535]

# remove the items into the list


list_items=[1,2,54,"santosh","peddinti",166.35]

list_items.remove("santosh")
list_items.remove("peddinti")

print(list_items)

# opt: [1, 2, 54, 166.35]

# clear the entire list

list_items=[1,2,54,"santosh","peddinti",166.35]

list_items.clear()

print(list_items)

# opt: []
