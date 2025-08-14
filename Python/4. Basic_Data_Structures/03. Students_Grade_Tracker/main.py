def find_student(students, name):
    name = name.strip().lower()
    
    for student in students:
        if student["name"].lower() == name:
            return student
    return None


def add_student(students, name):
    if not name.strip():
        print("❌ Student name cannot be empty.")
        return
    
    if find_student(students, name):
        print("⚠ Student already exists.")
        return
    
    students.append({"name": name.strip(), "grades": {}})
    print(f"✅ Student '{name.strip()}' added.")
    
def add_grade(students, student_name, subject, grade):
    student = find_student(students, student_name)
    
    if not student:
        print("❌ Student not found.")
        return
    
    if not subject.strip():
        print("❌ Subject name cannot be empty.")
        return
    
    try:
        grade = float(grade)
        if grade < 0 or grade > 100:
            print("❌ Grade must be between 0 and 100.")
            return
    except ValueError:
        print("❌ Invalid grade. Enter a number.")
        return
    
    student["grades"][subject.strip()] = grade
    print(f"✅ Grade {grade} added/updated for '{student_name.strip()}' in '{subject.strip()}'.")
    
def view_all(students):
    if not students:
        print("📭 No students to display.")
        return
    
    for student in students:
        print(f"\n👤 {student['name']}:")
        if student["grades"]:
            for subject, grade in student["grades"].items():
                print(f"  {subject}: {grade}")
        else:
            print("  No grades recorded.")
            
def student_average(students, student_name):
    student = find_student(students, student_name)
    if not student:
        print("❌ Student not found.")
        return
    
    grades = student["grades"].values()
    if not grades:
        print(f"ℹ '{student_name}' has no grades recorded yet.")
        return

    avg = sum(grades) / len(grades)
    print(f"📊 Average grade for '{student_name}': {avg:.2f}")

def search_student(students, student_name):
    student = find_student(students, student_name)
    if not student:
        print("❌ Student not found.")
        return

    print(f"\n👤 {student['name']}:")
    if student["grades"]:
        for subject, grade in student["grades"].items():
            print(f"  {subject}: {grade}")
        avg = sum(student["grades"].values()) / len(student["grades"])
        print(f"  Average: {avg:.2f}")
    else:
        print("  No grades recorded.")
        
def show_menu():
    print("\n🎓 Student Grade Tracker Menu")
    print("1. Add a new student")
    print("2. Add/update grade for a student")
    print("3. View all students and grades")
    print("4. Search for a student and view average")
    print("5. Exit")
    
def main():
    students = []
    
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            add_student(students, name)

        elif choice == "2":
            student_name = input("Enter student name: ")
            subject = input("Enter subject name: ")
            grade = input("Enter grade (0-100): ")
            add_grade(students, student_name, subject, grade)

        elif choice == "3":
            view_all(students)

        elif choice == "4":
            student_name = input("Enter student name: ")
            search_student(students, student_name)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1-5.")

if __name__ == "__main__":
    main()
