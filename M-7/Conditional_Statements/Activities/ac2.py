h = float(input("Input your height (cm): "))
w = float(input("Input your weight (kg): "))

bmi = w / ((h / 100) ** 2)

print("Calculated BMI:", bmi)

if bmi <= 18.4:
    print("Status: Underweight")
elif bmi <= 24.9:
    print("Status: Healthy")
elif bmi <= 29.9:
    print("Status: Overweight")
elif bmi <= 34.9:
    print("Status: Severely overweight")
elif bmi <= 39.9:
    print("Status: Obese")
else:
    print("Status: Severely obese")
