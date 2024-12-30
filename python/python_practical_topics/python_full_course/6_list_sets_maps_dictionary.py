
                                # 1. List


# create list

my_list=[1,5.5,"santosh","peddinti",True,False]

print(my_list)  # opt: [1,55,14,'santosh','peddinti',True,False]

# 1. append

my_list.append("gopinadh")

print(my_list) # opt: [1,5.5,'santosh','peddinti',True,False,'gopinadh']

# 2. extend

my_list.extend([5,3])

print(my_list)

# opt: [1,5.5 , 'santosh', 'peddinti' , True, False 'gopinadh' 5, 3]

# 3. insert(index, item)

my_list.insert(2,"jeevan")

print(my_list)

# opt: [1,5.5, 'jeevan','santosh','peddinti',True,'False','gopinadh',5,3]

# 4. remove(item)

my_list.remove("peddinti")

print(my_list)

# opt: [1,5.5, 'jeevan', 'santosh', True, False, 'gopinadh',5,3]

# 5.pop(item)

my_list.pop()

print(my_list)

# opt: [1,5.5, 'jeevan' 'santosh', True , False, 'gopinadh', 5]

# 6. sort ()

my_list1=[1,43,5,2,535,21,444,20]

my_list1.sort()

print(my_list1) # opt: [1, 2, 5, 20, 21, 43, 444, 535]


                        # 2. Set


# create the set
my_set = {1,44.4,15,7,51}

print(my_set) # opt: {1, 51, 7, 44.4, 15}

# add item

my_set.add(5)

print(my_set)  # opt: {1, 51, 5, 7, 44.4, 15}

# remove item

my_set.remove(44.4)

print(my_set)  # opt: {1, 51, 5, 7, 15}

# union set

my_set1={43,22,67,643}

union_set=my_set.union(my_set1) # opt: {1, 67, 643, 5, 7, 43, 15, 51, 22}

print(union_set)

# intersection_set

intersection_set=my_set | my_set1

print(intersection_set) # opt: {1,67, 643, 5, 7, 43, 15, 51, 22}

                      # 3. Dictionary

# create the dictionary

my_dict={"name":"santosh","last_name":"peddinti","address":"vizag"}

print(my_dict)

# opt: {'name':'santosh','last_name':'peddinti','address':'vizag'}

# get a key

get_key=my_dict.get("name")

print(get_key) # opt: santosh

# get keys

only_keys=my_dict.keys()

print(only_keys) # opt: dict_keys( ['name', 'last_name','address'] )

# get values

only_values=my_dict.values()

print(only_values) # opt: dict_values(['santosh', 'peddinti', 'vizag'])

# items

only_values=my_dict.items()

print(only_values)

# opt: ([('name', 'santosh'),('last_name','peddinti'),('address','vizag')])

# pop(key):

only_pop=my_dict.pop("name")

print(only_pop)    # opt: santosh

# pop

only_pop=my_dict.pop("address")

print(only_pop) # opt: vizag


                          # 4. Tuple

# create the list of numbers

list_tuple=(1,2,3,4,5)

print(list_tuple)  # opt: (1,2,3,4,5)

# print first three elements

print(list_tuple[:3])  # opt: (1,2,3)

# deleting the tuple
del_tuple=(1,2,3,4,5)

del del_tuple

print(del_tuple)  # opt: NameError: name 'del_tuple' is not defined


# SUMMARY

# list - ordered, mutable, allows duplicates. ex: [1,2,3]
# set - unordered, mutable, no duplicates. ex: {1,2,3}
# dictionary - unordered, key-value pairs.  ex: {'a':1,'b':2}
# tuples - similar to lists but it un mutable ex: (1,2,3)




