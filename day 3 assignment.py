##                         Day 3 assignment

##1, use IF ELSE and ELIF to write a program in python for your report cards

per=float(input("please enter percentage for grade  "))

if(per>=80):
    print("A grade")
elif(per>=70 and per<=80):
    print("B grade")
elif(per>=60 and per<70):
    print("C grade")
elif("per<59"):
    print("FAIL")
else:
    print("invalid result.......")


##2. use for loop to prime number in between 1 to 1000
for i in range(1, 1001):
    count=0
    for j in range(1, i + 1):
        if (i % j == 0):
            count = count + 1
    if (count == 2):
        print(i,end=' ')


##3.write a program for printing the tabels from 1,10 using nested for loop

for i in range(1,11):
    for j in range(1,11):
        print(i*j," ", end='')
    print()


##4.write a program to print x prime number using while loop, and take the input of x from the user

x = int(input(" please enter any number "))
count = 0
i = 2

while(i <= x//2):
    if(x % i == 0):
        count = count +1
        break
    i = i+1

if (count == 0 and x != 1):
    print(" %d is a prime number" %x)
else:
    print(" %d is not a prime number" %x)
        
