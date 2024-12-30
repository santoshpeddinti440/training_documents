
# loops

# for loop

n=int(input())

for i in range(1,n+1):
    print(i,"\n")

# input: 5
# output: 1 2 3 4 5


# break statement

for i in range(1,10):
    if i == 5:
        print("statement break - ",i)
        break
    print("statement -",i)

# output:

# statement - 1
# statement - 2
# statement - 3
# statement - 4
# statement break -  5

# pass statement:

for i in range(1,10):
    if i%3 == 0 or i%2 == 0:
        pass
    else:
        print(i,end=" ")

# output: 1, 5, 7

# for else statement

for i in range(1,10):
    if i == 5:
        print("if statement - ",i)
    else:
        print("else statement - ",i)

# output:

# else statement -  1
# else statement -  2
# else statement -  3
# else statement -  4
# if statement -  5
# else statement -  6
# else statement -  7
# else statement -  8
# else statement -  9

# Nested for

for i in range(1,4):
    print("For loop - ",i)
    for j in range(1,5):
        print("Nested loop - ",j)

# output:

# For loop -  1
# Nested loop -  1
# Nested loop -  2
# Nested loop -  3
# Nested loop -  4
# For loop -  2
# Nested loop -  1
# Nested loop -  2
# Nested loop -  3
# Nested loop -  4
# For loop -  3
# Nested loop -  1
# Nested loop -  2
# Nested loop -  3
# Nested loop -  4

# while loop

n=int(input())

i=1

while i<=n:
    print("statement - ",i)
    i+=1

# output

# statement - 1
# statement - 2
# statement - 3
# statement - 4
# statement - 5

# Nested loop:

n=int(input())

while n>9:
    s=0
    while n!=0:
        s=s+n%10
        n=n//10
    n=s
    print(n)

# input: 276
# output: 15,6



