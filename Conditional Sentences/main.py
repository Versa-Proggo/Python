weight = float(input(f"Enter your weight in kg: "))
height = float(input(f"Enter your weight in inches: "))
height = height * 0.0254
bmi = weight/height**2
if bmi < 18.5:
    print(f"Bmi is {bmi}, so you are under weight like Lucía Zárate")
elif bmi <25:
    print(f"Bmi is {bmi}, so you are healthy")
elif bmi <30:
    print(f"Bmi is {bmi}, so you are overweight")
elif bmi <35:
    print(f"Bmi is {bmi}, so you are obesey")
else:
    print(f"Bmi is {bmi}, so you are extremly obese")
