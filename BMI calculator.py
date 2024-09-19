# BMI calculator

weight=float(input("Enter yout weight in kg "))
height=float(input("Enter your height in meters "))

bmi= weight/(height)**2
print("BMI is",bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")