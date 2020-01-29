a=5.0
b=2
# what we wish to print is : a / b = ans
# to print ans what we do is

print(a/b)

# to print exactly a/b what we do is

print("a/b")

# so to get  a / b = ans, we should write
# print("a / b = " +  a/b) ?? ... try it
# we get a TypeError that string and int cannot be combined
# lets try to figure this out using simple exapmles
# what was the difference between a/b and "a/b"
# lets find out using a new command type()

print(5)
print(type(5))
print(a/b)
print(type(a/b))
print("a/b")
print(type("a/b"))

# its time to define the datatypes
# int - any positive or negative integer
# float - any positive or negative number with decimal point
# string - any text enclosed within " "

# some operations can be performed between different datatypes

print(5 + 2.0)
print(type(5 + 2.0))

# some datatypes only allow specific operations on them

print("word1 "+"word2 ")
print(type("word1 "+"word2 "))

# now, lets try to tackle our initial problem ... print : a / b = ans
# the solution to this problem is, to consider int(ans) as string while printing
# how do we express int as a string ??

print( str(a+b) )
print(type( str(a+b) ))

# now lets try to combine str and int togather

print("a + b = "+str(a+b))
print(type("a + b = "+str(a+b)))

# this has solved our problem
# we also got a method to convert one datatype to another

print(int("42"))
print(type(int("42")))
print(float("42"))
print(type(float("42")))

# this method is really really useful
# while we learn about user defined inputs

# Do you remember the comparison and identity operators?
# They gave answers as True or False
# what do you think was its datatype ? was it string ? ("True")

print(1==2)
print(type(1==2))

# True and False are called bool operators
# they can be represented using 1 - true and 0 - false

print(int(False))
print(type(int(False)))

print(bool(""))
print(bool(0))
print(bool(42))

# we also have a COMPLEX datatype in python ... YAY!!

print(4+2j)
print(type(4+2j))

# now you can play around with many mathematical formulae on python

# a really intersting property of python variables is that it can hold any datatype

x=5
print(type(x))
x=5.0
print(type(x))
x='5'
print(type(x))
x=5+0j
print(type(x))

# try finding an explanation to this
# this is due to pointer like variable storing system in python

# But what if you wish to use thousands of variables
# each of those variables may be of the same/different datatypes
# will you give them thousands of names ?
# frustrating ... right ?
# lets find out some solution in the next module

