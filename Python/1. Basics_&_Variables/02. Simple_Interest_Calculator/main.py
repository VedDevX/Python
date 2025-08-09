# Simple Interest Calculator 

# Ask the User about Principal amount
principal_amount = int(input("Enter the Principal Amount: "))

# Ask the user about rate of interest
rate_of_interest = int(input("Enter the Rate of Interest: "))

# Ask the user about Time
time_in_years = int(input("Enter the years: "))

# Apply the formula to calculate the Simple Interest
simple_interest = (principal_amount * rate_of_interest * time_in_years) / 100

# Print the result with round off
print(f"The Calculated Simple Interest is: {round(simple_interest)}")