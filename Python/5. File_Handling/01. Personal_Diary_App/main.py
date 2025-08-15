import datetime

DIARY_FILE = "diary.txt"

def add_entry(user_entry, current_date):
    with open(DIARY_FILE, "a") as file:
        file.write(f"{current_date}: {user_entry}\n")
        
    print("✅ Entry saved!")
    
def view_entry(DIARY_FILE):
    try:
        with open(DIARY_FILE, "r") as file:
            content = file.read()
            if content.strip() == "":
                print("📭 No entries found.")
            else:
                print("\n--- All Diary Entries ---")
                print(content)
    except FileNotFoundError:
        print("📭 No diary file found. Add your first entry!")
        
def search_entry(DIARY_FILE, keyword, found):
    try: 
        with open(DIARY_FILE, "r") as file:
            for line in file:
                if keyword in line.lower():
                    print(line.strip())
                    found = True
        
        if not found:
            print("❌ No matching entries found.")
    except FileNotFoundError:
        print("📭 No diary file found. Add your first entry!")

def show_menu():
    print("1. Add Entry")
    print("2. View all Entries")
    print("3. Search Entries")
    print("4. Exit \n")
    
def main():
    
    while True:

        show_menu()
        choice = input("Choose between (1-4): ")
        
        if choice == "1":
            user_entry = input("Enter the Entry: ")
            current_date = datetime.date.today().strftime("%Y-%m-%d")
            add_entry(user_entry, current_date)
        elif choice == "2":
            view_entry(DIARY_FILE)
        elif choice == "3":
            keyword = input("Enter keyword to search: ").lower()
            found = False
            search_entry(DIARY_FILE, keyword, found)
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid Choice!")
        
if __name__ == "__main__":
    main()