weight_input = input("Enter your weight in kilograms: ")
height_input = input("Enter your height in meters: ")

is_weight_valid = weight_input.replace('.', '', 1).isdigit()
is_height_valid = height_input.replace('.', '', 1).isdigit()

if is_weight_valid and is_height_valid:
    weight = float(weight_input)
    height = float(height_input)
    
    bmi_score = weight / (height ** 2)
    print(f"Your calculated BMI score is: {bmi_score:.2f}")
else:
    print("Error: Input is illegal. Please enter numbers only.")