import csv
import os

FILE_NAME = "students.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Maths", "Science", "English", "Total", "Percentage"])
        
def add_student(FILE_NAME, name, maths_marks, science_marks, english_marks, total, percentage):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, maths_marks, science_marks, english_marks, total, round(percentage, 2)])
    print(f"✅ Report card for {name} addded successfully! \n")
    
def view_students(FILE_NAME):
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader, None) # Skips header row
            students = list(reader)
            
        if not students:
            print("📭 No students recorded yet.\n")
            return
        
        print("\n📜 All Students Report Cards:")
        for row in students:
            print(f"Name: {row[0]}, Maths: {row[1]}, Science: {row[2]}, English: {row[3]}, Total: {row[4]}, Percentage: {row[5]}%")
        print()
    except FileNotFoundError:
        print("📭 No student file found. Add a student first!\n")
        
def search_student(FILE_NAME, name_search, found):
    name_search = name_search.strip().lower()
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if row[0].strip().lower() == name_search:
                    print(f"\n📌 Report Card for {row[0]}:")
                    print(f"Maths: {row[1]}, Science: {row[2]}, English: {row[3]}, Total: {row[4]}, Percentage: {row[5]}%")
                    found = True
                    break
        
        if not found:
            print("❌ Student not found.\n")
    except FileNotFoundError:
        print("📭 No student file found. Add a student first!\n")
        
def show_menu():
    print("1. Add Student")
    print("2. View all student")
    print("3. Search student")
    print("4. Exit")
    
def main():
    while True:
        show_menu()
        choice = input("Choose between (1-4): ")
        
        if choice == "1":
            name = input("Enter the name of student: ")
            maths_marks = float(input("Enter the maths marks: "))
            science_marks = float(input("Enter the science marks: "))
            english_marks = float(input("Enter the english marks: "))
            total = maths_marks + science_marks + english_marks
            percentage = total / 3
            add_student(FILE_NAME, name, maths_marks, science_marks, english_marks, total, percentage)
            
        elif choice == "2":
            view_students(FILE_NAME) 
            
        elif choice == "3":
            name_search = input("Enter the name of student: ")
            found = False
            search_student(FILE_NAME, name_search, found)
            
        elif choice == "4":
            print("👋 Exiting Student Report Card Generator. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-4.\n")
            
if __name__ == "__main__":
    main()