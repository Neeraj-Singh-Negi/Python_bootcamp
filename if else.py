#  WAP TO CHECK IF YOU ARE ELIGIBLE TO VOTE OR NOT


age=int(input("Enter your age "))
if (age>17):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# WAP TO CHECK WHETHER ELIGIBLE FOR GOVERNMENT OR PRIVATE JOB


#Method 1


age=int(input("Enter your age  "))
gender=input("Enter your gender ")
if(age>17 and gender=="female"):
    print("Eligible for government job ")
elif(age>17 and gender=="male"):
    print("Eligible for private jobs ")
else:
    print("Yoy are not eligible for any job ")


#Method 2


age=int(input("Enter your age  "))
gender=input("Enter your gender ")
if(age>17):
    if(gender=="female"):
        print("you are eligible for government job")
    elif(gender=="male"):
        print("you are eligible for private job")
    else:
        print("your gender not exists")
else:
    print("you are not eligible for any job")


# WAP TO CHECK THE GREATEST AMONG THREE NUMBERS


a=float(input("Enter first number "))
b=float(input("Enter second number "))
c=float(input("Enter third number "))
if(a>b and a>c):
    print("a is greater")
elif(b>a and b>c):
    print("b is greater")
else:
    print("c is greater")