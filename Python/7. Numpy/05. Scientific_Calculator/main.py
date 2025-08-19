import numpy as np

def show_menu():
    print("\n🧮 Scientific Calculator Menu")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log, log10)")
    print("11. Factorial (!)")
    print("12. Absolute Value (abs)")
    print("13. Round Number")
    print("14. Exit")

def calculator():
    while True:
        show_menu()
        choice = input("Choose an operation (1-14): ").strip()

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {a + b}")

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {a - b}")

        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print(f"Result: {a * b}")

        elif choice == "4":
            a = float(input("Enter numerator: "))
            b = float(input("Enter denominator: "))
            if b == 0:
                print("❌ Cannot divide by zero!")
            else:
                print(f"Result: {a / b}")

        elif choice == "5":
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print(f"Result: {np.power(a, b)}")

        elif choice == "6":
            a = float(input("Enter number: "))
            if a < 0:
                print("❌ Cannot take square root of negative number!")
            else:
                print(f"Result: {np.sqrt(a)}")

        elif choice == "7":
            a = float(input("Enter angle in degrees: "))
            print(f"Result: {np.sin(np.radians(a))}")

        elif choice == "8":
            a = float(input("Enter angle in degrees: "))
            print(f"Result: {np.cos(np.radians(a))}")

        elif choice == "9":
            a = float(input("Enter angle in degrees: "))
            print(f"Result: {np.tan(np.radians(a))}")

        elif choice == "10":
            a = float(input("Enter number: "))
            if a <= 0:
                print("❌ Logarithm undefined for zero or negative numbers!")
            else:
                print(f"Natural log: {np.log(a)}, Base 10 log: {np.log10(a)}")

        elif choice == "11":
            a = int(input("Enter a non-negative integer: "))
            if a < 0:
                print("❌ Factorial not defined for negative numbers!")
            else:
                print(f"Result: {np.math.factorial(a)}")

        elif choice == "12":
            a = float(input("Enter number: "))
            print(f"Result: {np.abs(a)}")

        elif choice == "13":
            a = float(input("Enter number: "))
            print(f"Rounded Result: {np.round(a)}")

        elif choice == "14":
            print("👋 Exiting Scientific Calculator. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Enter 1-14.")

if __name__ == "__main__":
    calculator()
