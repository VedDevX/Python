# BMI Calculator 

# Get the User's weight
weight = float(input("Enter your weight (in Kilograms): "))

# Get the User's height
height = float(input("Enter your height (in Meters): "))

# Calculate the BMI Using Formula
BMI = (weight / (height)**2)

# Print the BMI Value
print(f"Your BMI value is: {BMI:.2f}")