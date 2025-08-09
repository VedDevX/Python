# Celsius to Faherenhite

# Asking the user about input 
celsius = float(input("Enter the temperature (Celsius): "))

# Formula to convert celsius to faherenite
fahrenhite = (celsius * 9/5) + 32

# Print the Conversion with rounding off
print(f"Temperature is {fahrenhite:.3f} Fahrenhite.")



# Fahrenhite to Celsius 

# Ask the user about input 
fahrenhite_input = float(input("Enter the temperature (Fahrenhite): "))

# Formula  to convert fahrenhite to celsius
celsius_output = (fahrenhite_input - 32) * 5/9

# Using the round() Function
rounded_celsius_value = round(celsius_output, 1)

# Print the conversion with rounding off
print(f"Temperature is {rounded_celsius_value} Celsius.")