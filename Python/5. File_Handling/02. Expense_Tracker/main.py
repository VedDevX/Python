import csv
import os

FILE_NAME = "expenses.csv"

# Create file with header if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:  # newline='' prevents blank lines
        writer = csv.writer(file)
        writer.writerow(["Date", "Description", "Amount"])

def add_expense(FILE_NAME, date, description, amount):
    # (optional) basic validation
    if not date.strip() or not description.strip() or not amount.strip():
        print("❌ Please enter date, description, and amount.\n")
        return
    try:
        float(amount)  # just to ensure it’s numeric
    except ValueError:
        print("❌ Amount must be a number.\n")
        return

    # IMPORTANT: use newline='' when writing/appending CSV
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, description, amount])
    print("✅ Expense added successfully! \n")

def view_expense(FILE_NAME):
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)  # skip header safely

            rows = []
            for row in reader:
                # Skip empty/malformed rows
                if len(row) < 3:
                    continue
                rows.append(row)

        if not rows:
            print("📭 No expenses recorded yet.")
            return

        print("\n📜 All Expenses:")
        for row in rows:
            print(f"Date: {row[0]}, Description: {row[1]}, Amount: ₹{row[2]}")
        print()
    except FileNotFoundError:
        print("📭 No expense file found. Add your first expense!")

def total_expense(FILE_NAME):
    total = 0.0
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None)  # skip header safely
            for row in reader:
                # Skip empty/malformed rows
                if len(row) < 3:
                    continue
                try:
                    total += float(row[2])
                except ValueError:
                    # Skip rows where amount isn't numeric
                    continue
        print(f"\n💰 Total Expenses: ₹{total} \n")
    except FileNotFoundError:
        print("📭 No expense file found. Add your first expense!\n")

def show_menu():
    print("1. Add Expense")
    print("2. View all Expenses")
    print("3. View total Expenses")
    print("4. Exit \n")

def main():
    while True:
        show_menu()
        choice = input("Choose between (1-4): ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = input("Enter Amount: ")
            add_expense(FILE_NAME, date, description, amount)

        elif choice == "2":
            view_expense(FILE_NAME)

        elif choice == "3":
            total_expense(FILE_NAME)

        elif choice == "4":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
