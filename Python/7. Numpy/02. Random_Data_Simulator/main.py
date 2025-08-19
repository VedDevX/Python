import numpy as np

def random_integers():
    low = int(input("Enter the minimum value: "))
    high = int(input("Enter the maximum value: "))
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    data = np.random.randint(low, high+1, size = (rows, cols))
    print("\nGenerated Random Integers:\n", data)
    
def random_floats():
    low = float(input("Enter the minimum value: "))
    high = float(input("Enter the maximum value: "))
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    data = np.random.uniform(low, high, size=(rows, cols))
    print("\nGenerated Random Floats:\n", data)
    
def random_normal():
    mean = float(input("Enter the mean: "))
    std = float(input("Enter the Standard Deviation: "))
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    data = np.random.normal(mean, std, size=(rows, cols))
    print("\nGenerated Normal Distribution Data:\n", data)
    
def random_choice():
    items = input("Enter items seperated by commas: ").split(",")
    count = int(input("How many random choices do you want? "))
    data = np.random.choice(items, size=count)
    print("\nRandomly Chosen Items:\n", data)
    
def show_menu():
    print("\n🎲 Random Data Simulator")
    print("1. Random Integers")
    print("2. Random Floats (Uniform Distribution)")
    print("3. Random Numbers (Normal Distribution)")
    print("4. Random Choice from a List")
    print("5. Exit")
    
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            random_integers()
        elif choice == "2":
            random_floats()
        elif choice == "3":
            random_normal()
        elif choice == "4":
            random_choice()
        elif choice == "5":
            print("👋 Exiting Random Data Simulator. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    main()