# Swaping


# 1. Swap two numbers without using a third variable.

# Method 1

a = 10
b = 50

a = a + b
b = a - b
a = a - b

print("a = ", a)
print("b = ", b)


# Method 2

a = 10 
b = 50

a = a * b
b = a / b
a = a / b

print("a = ", int(a))
print("b = ", int(b))



# Method 3

a = 10
b = 50

(a , b) = (b , a)

print("a = ", a)
print("b = ", b)




# 2.  Swap two numbers using a third variable.


a = 10
b = 50

temp = b
b = a
a = temp

print("a = ", a)
print("b = ", b)




