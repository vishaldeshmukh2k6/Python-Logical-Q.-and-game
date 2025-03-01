print("Hello, World");


# 1. what is variables

    # variable is a container that store data 

# Data Types

    # 1. Text Type:	str

    # Numeric Types:	int, float, complex

    # Sequence Types:	list, tuple, range

    # Mapping Type:	dict

    # Set Types:	set, frozenset

    # Boolean Type:	bool

    # Binary Types:	bytes, bytearray, memoryview

    # None Type:	NoneType



# strring


name = "Tikaram Gahane"  
print(name)                  # single code In on line Output
print(len(name))             # length of all string


name = """Tikaram

Gahane"""     

print(name)          # Triple code In more line Output. 
print(len(name))     # Length of all string.
print(name[0])       # print start the frist digit in string.
print(name[-5])      # print start the last digit in string.
print(name[0:15])
print(name[0:])
print(name[:])
print(type(name))    # check the what is class.


# Escape charector

    # Not add Escape charector

a = "Hay I am a 'Vishal Deshmukh'"
b = 'Vishal "Deshmukh"'
print(a)
print(b)

# Numeric Types

a = "Hay I am a \"Vishal Deshmukh\""
b = "Vishal \"Deshmukh\""
print(a)
print(b)


b = 'Vishal \\\ "Deshmukh"'
print(b)


b = 'Vishal \n"Deshmukh"'
print(b)



# Formeting

a = "Vishal"
b = "Deshmukh"

print(a + "" + b)

full_name =f"Name:{a} {b} {len(a)} {len(b)}"   # Formeting......Sttring
print(full_name)

# 1. integer

a = 10
print(type(a))

b = 11111
print(type(b))


# 2. float

a = 22.4
print(type(a))

b = 0.1
print(type(b))

# 3. complex

a = 23j
print(type(a))

b = 12j
print(type(b))

# String Method



name = "               vishal deshmukh               " 

print(name.upper())      # All text in capital letter.
print(name.lower())       # All text in small letter.
print(name.title())       # Frist letter capital.
print(name.strip())         # All space remove Starting and Ending.
print(name.lstrip())        # Left side space remove.
print(name.rstrip())        # Right side space remove.



# Find Method

name = "Pratik Deshmukh"

# new_name = name.find("tik")
# new_name = name.find("kh")
# new_name = name.find("Pra")
new_name = name.find("e")
print(new_name)


# Replace Method


name = "Tikaram Gahane"

# new_name = name.replace("Tikaram","Vishal")
# new_name = name.replace("Gahane","Deshmukh")
# new_name = name.replace("T","t")
# new_name = name.replace("G","0")
# new_name = name.replace("T","1")
# new_name = name.replace("m","10000000000000000000000")
# new_name = "Tikaram" in name
# new_name = "ram" in name
# new_name = "Vishal" in name
new_name = "Vishal" not in name

print(new_name)



# Number in Python


# Integer

a = 10
print(type(a))

a1 = 20
print(type(a1))


# Float 

a = 12.5
print(type(a))

a1 = 0.5
print(type(a1))


a = 10
b = 30

sum = a + b  # Addition
print(sum)

sum = a - b  # Subtraction
print(sum)

sum = a * b  # Multiplication
print(sum)

sum = a ** b # Exponent
print(sum)

sum = a / b  # Dviision
print(sum)

sum = a // b  # Flore
print(sum)

sum = a % b   # Modules
print(sum)


# Fuction for Numbers

# 1. round function

num = 2.9

# sum = round(num) 
# print(sum)
print(round(num)) # short 

num = 1.6

# sum = round(num)
# print(sum)
print(round(num)) # short 


# 2.  abs Function :- ( "This Function convert negitive to positiv" )


num = -1.6

# sum = abs(num)
# print(sum)
print(abs(num)) # short 


# math function :- ya function us kam ka h agr num ke bad point ho or usme kuch snkhya ho to direct age ki sakhya de deta h.

import math  

num = 1.6

print(math.ceil(num)) # short 


num = 0.6

print(math.ceil(num)) # short 


num = 1.6

sum = math.ceil(num)
print(sum)

# print(math.ceil(num)) # short 


# Floor function  :- Lower limit

num = 1.6

sum = math.floor(num)
print(sum)

# print(math.floor(num)) # Short


num = 4.05

sum = math.floor(num)
print(sum)

# print(math.floor(num))  # Short


num = 9.999
sum = math.floor(num)
print(sum)

# print(math.floor(num))  # Short




# Input form user


# print("Enter Your Name :-")
# name = input()
# print(f"Gm, {name}")

# print("Enter Your Name :-")

# name = input("Enter Your Name :-")
# print(f"Name :- {name}")

# Type Conversion

a = 10
b = 10.5
c = 1j

print(type(a))  # check type
print(type(b))  # Check type
print(type(c))  # Check type


# a = float(a)   # Convet int to float type.
a = complex(a)   # convert int to complex.
print(type(a))   # Print type
print(a)



b = int(b)      # Convet float to int.
print(type(b))  # print type
print(b)


a = "1"             # adding string
result = a + "1"
print(result)

a = "1"             # adding string and c.onvert the string in int.
result =int(a) + 1
print(result)



# Boolean 

# only two type :- "True and False"
# "",0, none = False else True

My_name_is_Vishal = True
print(type(My_name_is_Vishal))


a = "False"
a = bool(a)
print(type(a)) 
print(a)


# a = None     # This three input using output is False
# a = ""
a = 0
a = bool(a)
print(type(a)) 
print(a)


# use

# name = input("Enter your Name :-")
# print(name)


# num = input("Enter a Number :-")
# num = int(num) + 10
# print(num)


# Implicit Conversion

# 1. this only one example.

a = 10     #int   
b = 10.5   #float 

sum = a + b 


print(sum) # 20.5  :- python automatic a variable int convert in float.
print(type(sum)) # class Float


# 2. 

a = 20 # int to float convert automatic.
b = 2  # int to float convert automatic.

result = a / b

print(result)
print(type(result))  

# # 2.

# a = 10.5
# b = 20.4

# a = int(a) # Convert float to int.
# b = int(b) # Convert float to int.

# sum = a + b
# print(sum)

# # 3.

# a = 10
# b = 20

# a = float(a) # int convert to float.
# b = float(b) # int convert to float.

# sum = a + b
# print(sum)


# Operator in Python


# 1. Comparison Operators :- This is boolean Expression ( True and False )


# 1. Greter Than :-  ( > )
# 2. Less Than :- ( < )
# 3. Greter Than Equal to :- ( >= )
# 4. Less Than Equal to :- ( <= ) 
# 5. Equal to :- ( == )
# 6. Not equal to :- ( != )

a = 10
b = 5

# com = a < b       # Greter than
# com = a > b       # less than
# com = a <= b      # greter than equal to
# com = a >= b      # Less than equal to
# com = a == b      # Equal to
com = a != b      # Not equal to


print(com)


# ascii value

a = "vishal"
b = "muskan"

# com = a > b
com = a < b

print(com)

print(ord("v")) # Check the ascii value.
print(ord("i")) # Check the ascii value.
print(ord("A")) # Check the ascii value.




# Conditional statement 

# 1. If statement

 

physics = 75

if physics >= 45:
    print("Result :- Pass")
if physics < 45:
    print("RESULT :- FAIL")


maths = 30

if maths >= 45:
    print("RESULT :- PASS")
if maths < 45:
    print("RESULT :- FAIL")


English = 45.5

if English >= 45:
    print("RESULT :- PASS")
if English < 45:
    print("RESULT :- FAIL")


Marathi = 50

if Marathi >= 45:
    print("RESULT :- PASS")
if Marathi < 45:
    print("RESULT :- FAIL")

Hindi = 30

if Hindi >= 45:
    print("RESULT :- PASS")
if Hindi < 45:
    print("RESULT :- FAIL")


# if and else Stetement 


maths = 80

if maths >= 45:
    print("RESULT :- PASS")
else:
    print("RESULT :- FAIL")



physics = 30

if physics >= 45:
    print("RESULT :- PASS")
else:
    print("RESULT :- FAIL")


Marathi = 45

if Marathi >= 45:
    print("RESULT :- PASS")
else:
    print("RESULT :- FAIL")



# Logical Opratoer 

# and : True if both oprends are true X and Y 
        # Hindi
               # Python mein and operator tabhi True return karta hai jab dono expressions True hon.
               # Agar ek bhi False ho, to result False hoga.

# or  : True if either of the oprands is true X or Y

        # Hindi
        # Python mein or operator tabhi True return karta hai jab koi ek expression True ho.
        # Agar dono False hon, tabhi False hoga.

# not : True is operand if false not X
    #    Hindi

        # Python mein not operator ek expression ka ulta kar deta hai:
               # True ko False aur False ko True.


 #  and

# SSC = int(input("Enter the SSC Persentage :- ")) 
# HSC = int(input("Enter the HSC Persentage :- "))

# if SSC >= 60 and HSC >= 60 :
#     print("Eligible")
# else:
#     print("Not Eligible")



# or

# SSC = int(input("Enter the SSC Persentage :- ")) 
# HSC = int(input("Enter the HSC Persentage :- "))

# if SSC >= 60 or HSC >= 60 :
#     print("Eligible")
# else:
#     print("Not Eligible")

# not 


Criminal = True
# Criminal = False


# if Criminal == False:
if not Criminal:
    print("Eligible")
else:
    print("Not Eligible")

# Shortcircuit 


#  what is shortcircuet

# Python mein short-circuiting ka matlab hai jaise hi ek logical expression ka result pata chal jaaye, 
# baaki ka evaluate kiye bina ruk jaana, taaki performance achhi rahe aur errors se bacha ja sake.

# and oprator shortcircuet

# SSC = int(input("Enter the SSC Persentage :- ")) 
# HSC = int(input("Enter the HSC Persentage :- "))      
# Test = int(input("Enter the test mark :- "))

# if SSC >= 60 and HSC >= 60 and Test >= 60:     # All condition True  to Condition is Eligible
    # print("Eligible")
# else:
    # print("Not Eligible")


# or operoter in shortcircuet

# SSC = int(input("Enter the SSC Persentage :- ")) 
# HSC = int(input("Enter the HSC Persentage :- "))
# Test = int(input("Enter the test mark :- "))

# if SSC >= 60 or HSC >= 60 or Test >= 60:       # Any one condition True to Eligible
#     print("Eligible")
# else:
#     print("Not Eligible")


# Ternary oprator


# not add Ternary oprator

# age = int(input("Enter your age :- "))

# if age >= 18:
#     print("Can vote")
# else:
#     print("Can not vote")

# age = int(input("Enter your age :- "))

# print("Can vote") if age >= 18 else print("Can not vote")  

# The short trick of Ternary oprator ( Only one condition to apply)

# chaining comparison oprator

# age = int(input("Enter your age :- "))

# # if age >= 18 and age <= 28:
# if 18 <= age <= 28:
#     print("Eligible for Exam")
# else:
#     print("Not Eligible for Exam")


# Loop in Python  

# what is Loop ? 

(English)
#A loop in Python is a control flow statement that allows you to repeat a block of code multiple times.
#There are two main types of loops in Python:

(Hindi)
# Python mein loop ek control flow statement hai jo aapko ek block of code ko baar-baar chalane ki suvidha
# deta hai. Do main types ke loops hote hain:

# for loop:

(English) 
# Used to iterate over a sequence (like a list, tuple, or string).

(Hindi)
# Yeh sequence (jaise list, tuple, ya string) ke har element par iterate karta hai.

# while loop: 

(English)
# Repeats as long as a certain condition is true.

(Hindi)
# ab tak ek condition true rahti hai tab tak repeat karta hai.


# for loop 

# it`s use for itreble object 
 
# Ex. 1

# for x in range(3):
# for x in range(10 , 20):  # app diside kr skte ho kaha se start karna h kaha se end karna h ! 
for x in range(10 , 20 , 2):  #  11 , 13 , 15 , 17 , 19

    # print("Vishal Deshmukh")
    # print("Muskan Deshmukh")
    # print(100, x)
    print(100, x + 1)

# Ex. 2
 
# Print even and odd number using for loop ?

for number in range(1 , 101):
    if number % 2 == 0 :
        print("Even Number :- ",number)
    else:
        print("Odd Number :- ",number)

# EX. 3

# any number math table 

for number in range(1, 11):
    print(f"2 x {number} = {number * 2}")
    # print(f"3 x {number} = {number * 3}")
    # print(f"4 x {number} = {number * 4}")
    # print(f"5 x {number} = {number * 5}")
    # print(f"6 x {number} = {number * 6}")
    # print(f"7 x {number} = {number * 7}")
    # print(f"8 x {number} = {number * 8}")
    # print(f"9 x {number} = {number * 9}")
    # print(f"10 x {number} = {number * 10}")
    

# string  also itreble object

# Ex. 1

# name = "Vishal Deshmukh"
name = "Muskan Deshmukh"

for cha in name :  # This loop print one by one charector !
    print(cha)


# List Example in for loop ?

cart = ["Apple","Mango","Orange"]
# cart = ["Apple :- 10rs ", "Mango :- 20rs", "Orange :- 30rs","Total = 60rs"]

for item in cart :
    print(item)




# While loop in python

# what is while loop ?
#    :- loop as long as the variable is True 

# Example 1.  1 t0 10 number Print in Loop ?

# num = int(input("Enter the Frist Number :- "))
# last_num = int(input("Enter the last Number :- "))
# while num <= last_num:
#     print(num)
#     num = num + 1
# print("End")


# Example 2. Table print any table ?

# Number = int(input("Enter the which number of table :- "))
# i = 1
# while i <= 10:
#     Table = i * Number
#     print(Table)
#     i = i + 1

# Example 3. print odd even Number ?

# starting_number = int (input("Enter the starting Number :- "))
# Ending_Number = int (input("Enter the Ending Number :- "))


# while starting_number <= Ending_Number:         # This is While Condition.
#     if starting_number % 2 == 0:                # This is If Condition.
#         print("Even Number :- ",starting_number)
#     else:
#         print("Odd Number :- ", starting_number)
#     starting_number = starting_number + 1

    

# Example 4. Even odd sum print ?


# Frist_Number = int (input("Enter the Frist Number :- "))
# Last_Number = int (input("Enter the Last Number :- "))
# Even_Sum = 0
# Odd_sum = 0

# while Frist_Number <= Last_Number:
#     if Frist_Number % 2 == 0:
#         print("Even Number :- ",Frist_Number)
#         Even_Sum = Even_Sum + Frist_Number
#     else:
#         print("Odd Number :- ",Frist_Number)
#         Odd_sum = Odd_sum + Frist_Number
#     Frist_Number = Frist_Number + 1

# print("Even Number Sum :- ", Even_Sum)
# print("Odd Number sum :- ", Odd_sum)


# Write a all even Number till N

# N = int(input("Enter the N :- "))
# i = 1

# while i <= N:
#     if i % 2 == 0:
#         print(i)
        
#     i = i + 1

# Write a all odd Number till N


# N = int(input("Enter the N :- "))
# i = 1

# while i <= N :
#     if i % 2 != 0:
#         print(i)
#     i = i + 1         


# Break Stetement 

# in for loop

for x in range(10):
    # if x == 5:
    # if x == 6:
    if x == 1:
        break      # This is a breck stetament is means stop loop !
    print(x)


# In while loop

x = 1

while x <= 10:
    if x == 5:
        break
    print(x)
    x = x + 1



# continue in python


# in for loop


for x in range(10):
    if x == 3 or x == 9:   # or is a logical operator its use any one condition True is this condition True
        continue           # This use skip that number and start next number.
    print(x)


# In while loop


x = 0

while x < 10 :
    x = x + 1                # x value add 1 
    # if x == 2 or x == 5:
    # if x == 1 or x == 2:
    if x == 3 or x == 9:
        continue
    print(x)
    




# Using Else stetement with for loop and while loop ! 


# 1. Else stetament using for loop.

# Simple Game user input even number to loss user and input odd number user win ( Only Three chance )!


# for number in range(3):
#     num = int(input("Enter the odd Number :- "))

#     if num % 2 == 0 :
#         print("You loss!")
#         break
# else:
#     print("You win!")

# 2. Else stetament using while loop.


# x = int(input("Enter the Even Number :- "))

# while x <= 1000000000000000000000000000000000000000000000000000000000:   # Unlimited
#     if x % 2 == 0:
#         print("You Win !")
#         break
#     else:
#         print("You Loss !")
#         break




# Nested Loop 


# In for loop


# Ex.1


# for num1 in range(10):
#     for num2 in range(5):
#         print(f"{num1}, {num2}")
#     # print("---------------------")


# Ex. 2 :- Math Table.. 1 to 10 


for x in range(2,11):
    print(f"Table of {x}")
    for y in range(1, 11):
        print(f"{x} X {y} = {x * y}")
    print("-----------------")





# imp   ( end="")   ye apka output ko line me layega 


# Ex. 3 :- Pattern Question 

for x in range(1, 6):            # starting and ending Number 
    for y in range(1, x + 1):    # 
        print("*", end=" ")
    print("\n")                   # This tag Automatic line change  

    
# Ex. 4

# for x in range(1, 11):
#     print(f"{2} x {x} = {x * table}")
# In while loop 


# Ex. 1


# line = 1

# while line <= 5:
#     star = 1
#     while star <= line :
#         print("*", end=" ")
#         star = star + 1
#     print("\n")
#     line = line + 1






# number = int(input("Enter number or table :- "))

# x = 1 

# while x <= 10:
#     table = x * number
#     print(table)
#     x = x + 1


#   Print a single number table ? 

# table = int(input("Enter number or table :- "))

# for x in range(1, 11):
#     print(f"{2} x {x} = {x * table}")
    



# Function 

# Ex. 1

def gm_gn():                     
    print("Good Morning")
    print("Good Night")

print("Function Create")

gm_gn()  #  Function Use

# Ex. 2 

def vishal():
    print("Hay I am Vishal Deshmukh")
    print("My Age is 18 ")
    print("I am from Maharastra")

vishal()     # Use a function 
# vishal()
# vishal()
# vishal()   any time use 

# Ex. 3

# def table():
#     which_table = int(input("Enter a which table Number :- "))
#     for x in range(1, 11):
#         print(f"{2} x {x} = {x * which_table}")


# table()

# Ex. 4

# def table1_to_10():
#     for x in range(2,11):
#         print(f"Table of {x}")
#     for y in range(1, 11):
#         print(f"{x} X {y} = {x * y}")
#     print("-----------------")


# table1_to_10()


# Ex. 5

# def pattern():
#     for x in range(1,6):    
#         for y in range(1, x + 1):
#             print("*", end=" ")
#         print("\n")


# pattern()

# Ex.6

# Even odd number print with function


# def Even_Odd():
#     number = int(input("Enter the last Number :- "))

#     x = 1

#     while x <= number:
#         if x % 2 == 0:
#             print("Even Number :- ", x) 
#         else:
#             print("Odd Number :- ", x)
#         x = x + 1
    

# Even_Odd()



# Argument and parameter

# Ex. 1

def hi_Hello(name):        # This Name is parameter     
    print(f"Hi {name}")
    print("Hello")


hi_Hello("Vishal")        # This vishal is Argument.


# Ex.2

def Full_From(address):
    print(f"Hay I am From {address}")   # This "address" is a parameter.
    print("Thank You !")

Full_From("Lobhi Village In Maharastra")   # This "Lobhi Village In Maharastra" is a Argument.  
Full_From("Fathepur in Himachal")          # This "Fathepur in Himach   al" is a Argument.


# Ex. 3


def middel_name(MN , LS ="Deshmukh"):
    print(f"Hay I am a Vishal {MN} {LS}")
    print("My Dad is Farmer ")

middel_name("Santosh")
  

# Ex. 4

def table(num):
    for x in range(1,11):
        print(f"{num} x {x} = {x * num}")


# table(3)
# table(4)
# table(11)
table(9)


# Keyword Argument


def middel_n(MN , LS):
    print(f"Hay I am a Vishal {MN} {LS}")
    print("My Dad is Farmer ")

# middel_n(LS = "Deshmukh", MN = "Santosh")
middel_n("Santosh", LS= "Deshmukh")   # ap frist Name Hata skte ho but last ya midel name nhi 
  


def Full_Name(fristname, secondname , lastname ):
    print(f"Hay I am a {fristname} my father name is {secondname} and my surname is {lastname}")


Full_Name("Vishal", secondname = "Santosh", lastname = "Deshmukh"  )



# Return in Function 




# def print_add(num1,num2):   # Isne kuch return nhi kiya!
#     # sum = num1 + num2
#     # print(sum)
#     # MUL = num1 * num2
#     div = num1 / num2
#     print(div)
# print_add(12,20)
# # w = print_add(12,20)
# # print(w)   # None




# Ex. 1

# def return_add(num1, num2):
#     result = num1 + num2
#     return result

# # print(return_add(10,11))
# s = return_add(10,11)
# print(s)


# Ex. 2

def return_notlimit(num1, num2):
    result1 = num1 * 2
    result2 = num2 * 2 
    result3 = num1 * num2
    result4 = num1 * 10
    return result1, result2, result3, result4 
    # return result1 + result2 + result3 + result4 

total1, total2, total3, total4 = return_notlimit(2,5)
# print(f"result1 = {total1}, result2 = {total2}, result3 = {total3}, result4 = {total4}")
print(f"Result1 :- {total1}")
print(f"Result2 :- {total2}")
print(f"Result3 :- {total3}")
print(f"Result4 :- {total4}")

# print(return_notlimit(2,5))




# *args in Python 


# Ex. 1

def tata(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print(sum)

tata(1,2,3,4,5,6,7,8,9,10)


# Ex. 2

def even(*even):
    for n in even:
        if n % 2 == 0:
            print(f"Even Number :- {n}")
        else:
            print(f"Odd Number :- {n}")

even(1,2,3,4,5,6,7,8,9,10)


# def odd(*odd):
#     for x in odd:
#         if x % 2 != 0:
#             print(f"Odd Number :- {x}")

# odd(1,2,3,4,5,6,7,8,9,10)


# Ex. 3


