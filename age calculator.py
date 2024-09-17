# Calculating age in years

current_year =input("Enter current year ")
born_year=input("Enter your birth year ")
current_age=int(current_year)-int(born_year)
print("Your current age is",current_age)

# Program to calculate age in years,months and days using function

from datetime import datetime

def calculate_age(birthdate):
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the age
    age = current_date - birthdate
    
    # Extract years, months, and days from the age
    years = age.days // 365
    months = (age.days % 365) // 30
    days = (age.days % 365) % 30
    
    return years, months, days

# Input the birthdate in the format yyyy, mm, dd
year = int(input("Enter the birth year: "))
month = int(input("Enter the birth month: "))
day = int(input("Enter the birth day: "))

birthdate = datetime(year, month, day)
years, months, days = calculate_age(birthdate)

print(f"Age: {years} years, {months} months, {days} days")