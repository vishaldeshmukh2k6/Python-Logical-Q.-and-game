# Variables Input and output


# 1. Write a program to take three variables to store your birth date, birth month, and birth year,
# respectively, and then print them one by one in a specified order.

Date_of_Birth = "07"
Birth_Month = "November"
Birth_year = "2006"

# DOB = Date_of_Birth + Birth_Month + Birth_year # all dob add
# print(DOB)


print(Date_of_Birth)
print(Birth_Month)
print(Birth_year)


# 2. Write a program to take input from the user, and then print it to the output.


# Number = input("Enter the Number :-")
# print(Number)


# 3. Imagine you and your friend have brought different snacks for lunch. However,
# you want to exchange your snacks with each other.
# To do this, you decide to enlist the help of a friend who can hold one snack box while
# you exchange with your other friend. Similarly, in programming,
# we can use a third variable to help us swap the values of two variables.




a = 10
b = 30

temp = b 
b = a
a = temp

print("a :-",a)
print("b :-",b)


# Arthmatic operator


# 4. Write a program to take two numbers from the user and perform Six basic operations 
# (addition, subtraction, multiplication, division, integer division and modulus) on those two numbers.

# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))
a = 10
b = 30


sum = a + b
sub = a - b
mul = a * b
div = a / b
idiv = a // b
mod = a % b

print(sum)
print(sub)
print(mul)
print(div)
print(idiv)
print(mod)


# 5. Write a program to take two numbers A and B from the user and calculate the quotient 
# and remainder when number A is divided by number B

a = 12
b = 5

mod = a // b
idiv = a % b

print(mod)
print(idiv)


a = 15
b = 6

mod = a // b
idiv = a % b

print(mod)
print(idiv)


 
 	
# 6.  Write a program to take a positive number from the user and then display the last digit of that number.


a = 123

last_digit = a % 10
print(last_digit)


b = 234

last_digit1 = b % 10
print(last_digit1)


# 7. Write a program to convert a temperature from Celsius to Fahrenheit using the formula  C/5 = (F-32)/9.

celsius = 30

fahrenheit =int(celsius * 9 / 5) + 32  # This is the formula.
print(fahrenheit)



celsius1 = 40

fit = int(celsius1 * 9 / 5) + 32
print(fit)


# From user input 

# celsius = int(input("Enter the celsius :- "))
Fahrenheit =int(celsius * 9 / 5) + 32

print(Fahrenheit)


# 8. Write a program to take two inputs from the user and swap them without using a temporary or third variable.


# Addition and subtraction

# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))

a = a + b
b = a - b
a = a - b

print("a :-",a)
print("b :-",b)


# Multiplication and division

# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))

a = int(a * b)
b = int(a / b)
a = int(a / b)

print("a :-",a)
print("b :-",b)


# 9. Write a program to take two numbers, A and B from the user. Your task is to find the largest number that 
# is less than A and can be divided evenly by B. Can you figure out that number?


# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))

mod = a // b    # flore Diviision
last = mod * b  # Multiplication

print(last)


# Condition

# 10. Write a program to take two numbers from the user and determine the greater of those two given numbers.

# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))

if a >= b:                      # Using condition
    print("A :- ",a)
else:
    print("B :- ",b)



 	
# 11. Write a program to take a number from the user and print that number as Odd or Even.

# Number = int(input("Enter the Number :- "))

# if Number % 2 == 0:
    # print("Even")
# else:
    # print("Odd")


  
 	
# 12. Write a program to take a number from the user and output whether that number is negative,
#  positive or zero.

# Number = int(input("Enter the Number :- "))

# if Number > 0:
#     print("Positive")
# elif Number >= 0:
#     print("Zero")
# else:
#     print("Negative")

# Ex . 1

# Total_mark =int (input("Enter The Total Mark :- "))

# if Total_mark > 250:
#     print("Grade :- A")

# elif Total_mark > 150:
#     print("Grade :- B")

# elif Total_mark > 100:
#     print("Grade :- C")

# else:
#     print("Grade :- D")

# 13. Write a program to take an integer as input and print the smallest positive integer
# that is a multiple of both 2 and n.

# Number = int(input("Enter the Number :- "))

# if Number % 2 == 0:
#     print(Number)
# else:
#     Number1 = Number*2
#     print(Number1)


# 14. Write a program to take three numbers from the user and print the greater number of the three numbers.
# (Assume all three numbers are distinct)


# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))
# c = int(input("Enter the Number C:- "))

# if a > b:
#     greter = a
# else:
#     greter = b
# if greter > c:
#     greter = greter
# else:
#     greter = c

# print("greter_Number :-",greter)


# 15. Write a program to take four numbers from the user and print the greater number of the four numbers.
# (assume all the numbers are distinct).


# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))
# c = int(input("Enter the Number C:- "))
# d = int(input("Enter the Number D:- "))

# if a > b:
#     greter = a
# else:
#     greter = b
# if greter > c:
#     greter = greter
# else:
#     greter = c
# if greter > d:
#     greter = greter
# else:
#     greter = d

# print("Greter Number :- ",greter)


# 16. Imagine you and your friends are exploring the concept of leap years. A leap year is a year that is
# evenly divisible by 4, except for years that are divisible by 100 but not divisible by 400.
# In simpler terms, it's a special year with an extra day in February (February 29th). You're curious 
# to know whether a particular year is a leap year or not.


# year = int(input("Enter the year :- "))

# if year % 400 == 0:
#     print("Leap Year :- ",year)
# elif year % 4 == 0:
#     if year % 100 != 0:
#         print("Leap Year :- ",year)
#     else:
#          print("Not Leap Year :-",year)
# else:
#     print("Not Leap Year :-",year)

  
 	
# # 17. Write a program to take 3 numbers from the user and output the second max of 3 numbers.
# # (First, do it in the normal way then do it by using 3 comparisons)


# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))
# c = int(input("Enter the Number C:- "))

# if a > b:
#     max = a
#     second_max = b
# else:
#     max = b
#     second_max = a
# if max > c:
#     max = max
#     second_max = c
# else:
#     max = c
#     second_max = max

# print(second_max)

  
 
 	
# 18. Imagine you're working as a payroll manager in a company, and your job is to calculate the gross salary
# of employees based on their basic salary and certain allowances. The gross salary includes the basic 
# salary along with House Rent Allowance (HRA) and Dearness Allowance (DA), which vary based on the employee'
# s basic salary range.

# Write a program to take the basic salary of an employee and calculate its Gross salary according to the 
# following: (Gross salary is the sum of basic salary, HRA, and DRA)
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 25%, DA = 90%
# Basic Salary > 20000 : HRA = 30%, DA = 95%


# Basic_salary = int(input("Enter the Basic salary :- "))

# if Basic_salary <= 10000:
#     HRA = Basic_salary * 20 / 100
#     DA = Basic_salary * 80 / 100
# elif Basic_salary <= 20000:
#     HRA = Basic_salary * 25 / 100
#     DA = Basic_salary * 90 / 100
# else:
#     HRA = Basic_salary * 30 / 100
#     DA = Basic_salary * 95 / 100

# Gross_salary = int(Basic_salary + HRA + DA)

# print(Gross_salary)


# 19. Imagine you're responsible for calculating electricity bills for households. Each household consumes 
# electricity, and the bill varies based on the number of units consumed. The bill calculation involves 
# different rates for different ranges of units consumed, along with an additional surcharge.

# Write a program  to input electricity unit charges and calculate the total electricity bill according to the 
# given condition:
# For the first 50 units Rs. 0.50/unit
# For the next 100 units Rs. 0.75/unit
# For the next 100 units Rs. 1.20/unit
# For units above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill


# Unit = int(input("Enter the Units :- "))

# if Unit >= 50:
#     bill = Unit * 0.50
# elif Unit <= 100:
#     bill = Unit * 0.75
# elif Unit <= 100:
#     bill = Unit * 1.20
# elif Unit <= 250:
#     bill = Unit * 1.50

# subcharge = bill * 20 / 100

# Total_bill = subcharge + bill

# print(Total_bill)


# This question iis not coomplete 


# 20.  Write a program to take 4 numbers from the user and output the third max of these 4 numbers.

# a = int(input("Enter the Number A:- "))
# b = int(input("Enter the Number B:- "))
# c = int(input("Enter the Number C:- "))
# d = int(input("Enter the Number D:- "))

# numbers = [a, b, c, d]

# third_max = numbers[2]  # 2 is indexing.

# print("The third maximum number is:", third_max)


# Loop 

# 23. Take the number N and the name from the user as inputs, and print the name N times.


# name = str(input("Enter a Name :- "))
# How_Many_Time_Print_Name = int(input("How Many Time print Name :- "))

# x = 1

# while x <= How_Many_Time_Print_Name:
#     print(name)
#     x = x + 1


# 24. Take a number N from the user as input, and print even numbers up to N.


# Using while loop


# last_number = int(input("Enter the last Number :- "))

# x = 1

# while x <= last_number:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1


# Using for loop 


# last_number = int(input("Enter the last Number :- "))


# for x in range(last_number):
#     x = x + 1
#     if x % 2 == 0:
#         print(x)



# 25. Write a program to print the sum of odd numbers up to N.


# using while loop

# N = int(input("Enter the N Number :- "))
# x = 1 
# sum = 0

# while x <= N :
#     if x % 2 != 0:
#         sum = sum + x
#     x = x + 1
# print(sum)


# using for loop 


# N = int(input("Enter the last number N :- "))    # Enter not same digit in for loop 100 hai to 101 dalo fir same ans ayega.

# x = 1
# sum = 0

# for x in range(N):
#     if x % 2 != 0 :
#         sum = sum + x
# print(sum)



# 26. Write a program to take two integers M, and N and print the sum of numbers in the range M to N.

# M = int(input("Enter the M Number :- "))
# N = int(input("Enter the N Number ;- "))    
# sum = 0

# using while loop

# while M <= N:
#     sum = sum + M
#     M = M + 1
# print(sum)



# using for  loop 

# for x in range(M, N):
#     sum = sum + x 
# print(sum + N)





# 27. Write a program to calculate the sum of the following series where N is input from the user.
# 1 + 1/2 + 1/3 + 1/4 + 1/5 +…………1/N


# N = int(input('Enter the N :- '))

# sum = 0

# using while loop 

# x = 1

# while x <= N:
#     add = 1/x
#     sum = sum + add
#     x = x + 1
# print(sum)


# Using for loop 


# for x in range(1,N):
#     add = 1 / x
#     sum = sum + add

# print((sum + 1/N))
    

# 28. Write a program to take a number from the user and print the number of digits in the given number.


# Number = int(input("Enter any digit of Number :- "))

# count = 0

# using while loop 

# while Number % 10:
#     count = count + 1
#     Number = Number // 10

# print(count)


# using for loop

# for x in range(Number):
#     if Number % 10:
#         count = count + 1
#         Number = Number // 10

# print(count)


# 29. Write a program to take a number from the user and print the sum of the digits of the given number.


# Number = int(input("Enter any digit of Number :- "))

# sum = 0

# using for loop 

# for x in range(Number):
#     single_n = Number % 10
#     sum = sum + single_n
#     Number = Number // 10

# print(sum)




# 30. 	Write a program to check if a number is a special type of number called a 'prime number'.
#  A prime number is a number that is only divisible by 1 and itself, and it doesn't have any other factors.








# 31. 	Write a program to take a number from the user and then determine if that number is a special type 
#       of number called a 'perfect number'

