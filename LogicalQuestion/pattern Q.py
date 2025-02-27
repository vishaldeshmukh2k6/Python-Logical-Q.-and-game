# *
# * *
# * * *
# * * * *
# * * * * *  



# This a pattern in using for loop and while loop .



# for loop 

for x in range(6):
    for y in range(1 , x + 1):
        print("*", end=" ")
    print("\n")



# while loop 


line = 1

while line <= 5:
    star = 1
    while star <= line :
        print("*",end=" ")
        star = star + 1
    print("\n")
    line = line + 1