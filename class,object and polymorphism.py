# Class and Object

class Neeraj:
    age=21
    print("Neeraj Singh Negi")
x=Neeraj()
print(x.age)

# Age Calculator using class and object

class Age_Calculate:
    current_year=int(input("Enter current year "))
    birth_year=int(input("Enter birth year "))
    age=current_year-birth_year
x=Age_Calculate()
print("Your age is ",x.age)


# Polymorphism

def age(dob):
    print(dob)
def age(dob,name):
    print(dob,name)
# x=age("19 Oct 1998")
y=age("20 Feb 1991","Mani Sharma")