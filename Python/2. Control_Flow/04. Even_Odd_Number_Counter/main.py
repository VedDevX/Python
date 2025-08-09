# Even / Odd Number Counter

first_number = int(input("Enter the first number: "))
last_number = int(input("Enter the last number: "))

even_count = 0
odd_count = 0

for number in range(first_number, last_number + 1):
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print(f"The Total even numbers between {first_number} to {last_number} is: {even_count}")
print(f"The Total odd numbers between {first_number} to {last_number} is: {odd_count}")