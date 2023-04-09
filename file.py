print("Welcome to the BMI (Body mass index) CALCULATOR ")
height = input("Please, enter your height in m: (example: 1.75)")
weight = input("Please, enter your weight in kg: ")
height_one=float(height)
weight_one=float(weight)
height_one_square=height_one**2
bmi= weight_one/height_one_square
bmi_bis=int(bmi)
bmi_tris= str(bmi_bis)
print("Your BMI is" +" "+ bmi_tris)
