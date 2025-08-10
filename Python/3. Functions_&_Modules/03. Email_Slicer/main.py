# Email Slicer

def email_slicer(email):
    username, domain = email.split('@')
    return username, domain

user_input = input("Enter the Email: ")

user_name, domain_name = email_slicer(user_input)

print(f"Username: {user_name}")
print(f"Domain Name: {domain_name}")