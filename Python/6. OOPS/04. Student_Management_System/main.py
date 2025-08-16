class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        print(f"✅ Grade {grade} added for {self.name}.")

    def calculate_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

    def display_info(self):
        avg = self.calculate_average()
        print(f"\n🎓 Student ID: {self.student_id}")
        print(f"👤 Name: {self.name}")
        print(f"🎂 Age: {self.age}")
        print(f"📊 Grades: {self.grades if self.grades else 'No grades yet'}")
        print(f"📈 Average: {avg:.2f}")


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"✅ Student {student.name} added successfully.")

    def remove_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            print(f"🗑 Student {student.name} removed successfully.")
        else:
            print("❌ Student not found.")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_all_students(self):
        if not self.students:
            print("📭 No students available.")
            return
        print("\n📚 All Students:")
        for student in self.students:
            student.display_info()


def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Add Grade to Student")
    print("4. View Student Details")
    print("5. View All Students")
    print("6. Exit")


def main():
    sms = StudentManagementSystem()

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            age = int(input("Enter Student Age: "))
            student = Student(student_id, name, age)
            sms.add_student(student)

        elif choice == "2":
            student_id = input("Enter Student ID to remove: ")
            sms.remove_student(student_id)

        elif choice == "3":
            student_id = input("Enter Student ID: ")
            student = sms.find_student(student_id)
            if student:
                grade = float(input("Enter grade: "))
                student.add_grade(grade)
            else:
                print("❌ Student not found.")

        elif choice == "4":
            student_id = input("Enter Student ID: ")
            student = sms.find_student(student_id)
            if student:
                student.display_info()
            else:
                print("❌ Student not found.")

        elif choice == "5":
            sms.display_all_students()

        elif choice == "6":
            print("👋 Exiting Student Management System. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
