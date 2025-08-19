import numpy as np

def input_matrix():
    rows = int(input("Enter the rows: "))
    cols = int(input("Enter the columns: "))
    print(f"Enter {rows*cols} elements row by row: ")
    
    elements = []
    
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"❌ Please enter exactly {cols} numbers.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))
        elements.append(row)
        
    return np.array(elements)


def show_menu():
    print("\n📌 Matrix Calculator Menu")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Inverse")
    print("7. Exit")

def main():
    print("=== Welcome to Matrix Calculator ===")

    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")
        
        if choice in ["1", "2", "3"]:
            print("\nEnter first matrix: ")
            A = input_matrix()
            print("\nEnter second matrix: ")
            B = input_matrix()
            
            if choice == "1":
                if A.shape == B.shape:
                    print("\n✅ Result of Addition:")
                    print(np.add(A, B))
                else:
                    print("❌ Matrices must have the same dimensions for addition.")
                    
            elif choice == "2":
                if A.shape == B.shape:
                    print("\n✅ Result of Subtraction:")
                    print(np.subtract(A, B))
                else:
                    print("❌ Matrices must have the same dimensions for subtraction.")
                
            elif choice == "3":
                if A.shape[1] == B.shape[1]:
                    print("\n✅ Result of Multiplication:")
                    print(np.matmul(A, B))
                else:
                    print("❌ Columns of first matrix must equal rows of second matrix.")
                    
        elif choice == "4":
            print("\nEnter a matrix:")
            A = input_matrix()
            print("\n✅ Transpose of Matrix:")
            print(np.transpose(A))
            
        elif choice == "5":
            print("\nEnter a square matrix:")
            A = input_matrix()
            if A.shape[0] == A.shape[1]:
                print("\n✅ Determinant of Matrix:", np.linalg.det(A))
            else:
                print("❌ Determinant can only be calculated for square matrices.")
                
        elif choice == "6": 
            print("\nEnter a square matrix:")
            A = input_matrix()
            if A.shape[0] == A.shape[1]:
                try:
                    print("\n✅ Inverse of Matrix:")
                    print(np.linalg.inv(A))
                except np.linalg.LinAlgError:
                    print("❌ This matrix is singular and has no inverse.")
            else:
                print("❌ Inverse can only be calculated for square matrices.")

        elif choice == "7":
            print("👋 Exiting Matrix Calculator. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1-7.")


if __name__ == "__main__":
    main()
