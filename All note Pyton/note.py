"""Python Syntax and Structure"""




x = 5            # int
y = 3.14         # float
name = "John"    # str
is_valid = True  # bool


# Basic Operators


#Arithmetic Operators:   +, -, *, /, //, %, **

#Comparison Operators:   ==, !=, <, >, <=, >=

#Logical Operators:      and, or, not


# Conditional Statements

# how to use if, elif, and else for decision-making

x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")


# Loops

#For Loop: Loop through sequences like lists, strings, or ranges

for i in range(5):
    print(i)   # 0,1,2,3,4



#while loop

count = 0
while count < 5:
    print(count)
    count += 1  # 0,1,2,3,4


# Functions

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")





""" Data Type """

#  Numeric Types

a = 22
b = -23
print(type(a))  # int
print(type(b))  # int

c = 12.4
d = -23.7
print(type(c)) # float
print(type(d)) # float

g = 1 + 2j
h = 2 - 5j
print(type(g)) # complex
print(type(h)) # complex


# Sequence Types
    
    # list

a = ['apple', 'banana', 1, 3.14]

print(type(a))  # list

    # tuple

b = ('apple', 'banana')
c = ('1','2','3')

print(type(b)) 
print(type(c)) 

    # range

r = range(0, 10)
t = range(0, 10000000)

print(type(r))
print(type(t))

# Mapping Type  (Dictionary)

person = {'name': 'John', 'age': 30}
a = {'name': 'pratik', 'age': 21}

print(type(person))
print(type(a))
# Set Types


my_set = set([1,2,3])
a = set([b,c,d])

print(type(my_set))
print(type(a))


''' common python data type '''

# int  ( Integer numbers )

    # Example  :  x = 5, x = 23, x =26545 , etc.


# float (Decimal numbers)

    # Example : x = 23.4 , x = 1.5 etc.


# complex (Complex numbers (real + imaginary))

    # Example : a = 23 + 34j, z = 2+2j , etc.

# str (Text strings)

    # Example : a = 'code', "python" , etc.

# list (Ordered collection (mutable))

    # Example : a = ["abc" , "bac"], name = ["vishal", "pratik", "santosh"]


# Ramdom number


import random
print(random.randrange(1,10))


# casting

a = 23

a = str(a)
print(type(a))
print(a)

b = 3.7

b = int(b)
print(type(b))
print(b)


c = 2

c = float(c)
print(type(c))
print(c)



a = """vishal"""

print(a)



# Slicing

# Accessing parts of the string

str = "navgurukul"
print(str[1:4])


str = "vishaldeshmukh"
print(str[ 0 :]) 
print(str[:len(str)])


str = "Tikaram"
print(str[0:len(str)])

str = "Muskan Shende"
print(str[0:])

a = 10 
print(a)