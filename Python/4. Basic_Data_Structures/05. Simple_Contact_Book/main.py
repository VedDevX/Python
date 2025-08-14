def add_contact(contacts, phones, emails, name, phone, email):
    """
    Add a new contact to the contact book.
    Ensures unique phone and email.
    """
    name = name.strip()
    phone = phone.strip()
    email = email.strip()

    if not name or not phone or not email:
        print("❌ Name, phone, and email cannot be empty.")
        return

    if name in contacts:
        print(f"⚠ Contact '{name}' already exists.")
        return

    if phone in phones:
        print(f"⚠ Phone '{phone}' is already used.")
        return

    if email in emails:
        print(f"⚠ Email '{email}' is already used.")
        return

    # Add contact
    contacts[name] = {"phone": phone, "email": email}
    phones.add(phone)
    emails.add(email)
    print(f"✅ Contact '{name}' added successfully.")

def view_contacts(contacts):
    """
    Display all contacts in the contact book.
    """
    if not contacts:
        print("📭 No contacts to display.")
        return

    print("\n📒 Contact List:")
    for i, (name, info) in enumerate(sorted(contacts.items()), start=1):
        print(f"{i}. {name} - Phone: {info['phone']}, Email: {info['email']}")

def search_contact(contacts, name):
    """
    Search for a contact by name and display details.
    """
    name = name.strip()
    contact = contacts.get(name)
    if contact:
        print(f"\n👤 {name} - Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print(f"❌ Contact '{name}' not found.")

def delete_contact(contacts, phones, emails, name):
    """
    Delete a contact from the contact book.
    Removes phone and email from sets to allow reuse.
    """
    name = name.strip()
    contact = contacts.pop(name, None)
    if contact:
        phones.discard(contact["phone"])
        emails.discard(contact["email"])
        print(f"✅ Contact '{name}' deleted.")
    else:
        print(f"❌ Contact '{name}' not found.")

# ------------------------
# User Interface
# ------------------------

def show_menu():
    print("\n📇 Contact Book Menu")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact by name")
    print("4. Delete contact")
    print("5. Exit")

def main():
    contacts = {}  # Dictionary: name -> {"phone": ..., "email": ...}
    phones = set() # Set of all used phone numbers
    emails = set() # Set of all used emails

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            add_contact(contacts, phones, emails, name, phone, email)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            name = input("Enter name to search: ")
            search_contact(contacts, name)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_contact(contacts, phones, emails, name)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1-5.")

if __name__ == "__main__":
    main()
