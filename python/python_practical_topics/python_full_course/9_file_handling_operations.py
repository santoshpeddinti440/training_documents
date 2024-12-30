

# open a file in read mode
file_operations=open("file_operations.txt")

# read file content
read_content=file_operations.read()

print(read_content)

# write file content

# open a file
file_operations=open("file_operations.txt",'w')

# write content to the file
file_operations.write('Programming is Fun. \n')
file_operations.write('Programming for devops engineer\n')

# close the file

# open a file
file_operations=open("file_operations.txt")

# read the file
read_content=file_operations.read()
print(read_content)

# #close the file
file_operations.close()

# checking if file is exist

import os

if os.path.exists("file_operations.txt"):
    print("file exists")
else:
    print("file doe's not exists")
