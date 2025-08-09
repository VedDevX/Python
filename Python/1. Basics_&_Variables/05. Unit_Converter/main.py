# Unit Converter (Kilometers -> Miles)

# Ask the User's about Kilometer 
Kilometer = int(input("Enter the Kilometers: "))

# Apply the Formula to convert kilometers to Miles
Miles = (Kilometer * 0.621371)

# print the conversion
print(f"{Kilometer} Km is a {Miles:.3f} Miles")

# Ask the User's about miles
miles_input = float(input("Enter the Miles: "))

# Apply the Formula to convert Miles to Kilometers
kilometer_output = (miles_input * 1.60934)

# Round off the Kilometer
kilometer_output = round(kilometer_output)

# Print the conversion
print(f"{miles_input} Miles is a {kilometer_output} Km")