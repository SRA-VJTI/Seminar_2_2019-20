# lets assume we need 10 variables
# each holding value from 1 to 10
# should we create 10 variables with different names, and assign them value?
# not really ... we have some datatypes that act as large containers
# they can hold many values in them unlike normal variables that holds just one value

a = [1,2,3,4,5,6,7,8,9,10]

# but what is it called? is it int ??

print(a)
print(type(a))

# so a list can hold many integers ... and floats, strings
# or even a combination of these datatypes

a = [False, 1, 2.0, '3', 4+0j]
print(a)

# but I wish to use just one variable from the list
# list elements can be accessed from their position numbers
# starting from 0

print(a[0])
print(type(a[0]))

print(a[1])
print(type(a[1]))

print(a[2])
print(type(a[2]))

print(a[3])
print(type(a[3]))

print(a[4])
print(type(a[4]))

# you can access a set of variables from a list
print(a[1:3])
#  if you need all elements from start upto a certain position
print(a[:3])
#  if you need all elements from a certain poition till end
print(a[3:])

# you can change elements in a list ... so its called a MUTABLE collection
a[0] = None
print(a)

# you can add or remove elements from list

a.append('I am new')
print(a)
a.remove('I am new')
print(a)
a.pop(2)
print(a)

# you can add, multiply, reverse, sort and do various things with list

a = [0,1]*5
print(a)
a = [1,4,7,2,8] + [3,5,10,6,9]
print(a)
a.sort()
print(a)
a.reverse()
print(a)

# lets have a look at the multiplication operator once again
a=[0,1]*5
print(a)

# Since you have understood lists, you will notice that
# even strings behave somewhat similarly

a = "aal izz well"
print(a[6])
a = a.replace("izz","is")
print(a)

# if i want to append a string after certain position
a = a[:6] + " not" + a[6:]
print(a)

# some powerful operations with strings
a = a.split()
print(a)
a = " ## ".join(a)
print(a)

# you cannot change elements of a string
# a[6] = 'y' is invalid ... try it
# so, strings are IMMUTABLE collections

# what if you wish to have an IMMUTABLE list
# its called a tuple

a = (1,2,3) + (4,5)
print(a)
print(type(a))

# tuple elements can be accessed the same way as list ... but cannot be changed
print(a[2])

# tuple can store variable data types
# tuples do not allow any modification in the position or value of its elements
# a really good use case for tuple is swapping

x=2
y=3
print(" x: "+ str(x) + " y: "+ str(y))
x,y = y,x
print(" x: "+ str(x) + " y: "+ str(y))

print(x,y)

# tuples may seem useless right now
# but they are extremely useful during function calls ... will be seen later

# Now, let us imagine that we have a contact list, which have to be saved in python
# you have a list of names, and one or more phone no. related to that person
# in what collection will you store it

# Behold!! Dictionary

a = {"alice":9876543210, "bob":9898989898, "oscar":9876556789}
print(a)
print(type(a))

print(a["bob"])

# you can use list, tuple, dictionary, set inside any other container

a["oscar"] = (9111191191, 8765678987)
print(a)

print(type(a["oscar"][1]))