import os

LOG_FILE = "sample.log"

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as file:
        file.write(
            "INFO: Server started\n"
            "WARNING: Disk space low\n"
            "ERROR: Failed to connect to database\n"
            "INFO: User login successful\n"
            "ERROR: Timeout while connecting\n"
            "WARNING: High memory usage\n"
        )
        
def analyze_log(LOG_FILE, total_lines, info_count, warning_count, error_count):
    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                total_lines += 1
                
                if line.startswith("INFO"):
                    info_count += 1 
                
                elif line.startswith("WARNING"):
                    warning_count += 1
                    
                elif line.startswith("ERROR"):
                    error_count += 1
        
        print("\n📊 Log File Summary:")
        print(f"Total lines: {total_lines}")
        print(f"INFO: {info_count}")
        print(f"WARNING: {warning_count}")
        print(f"ERROR: {error_count}\n")
        
    except FileNotFoundError:
        print("❌ Log file not found. Please ensure sample.log exists.")
        
def view_errors(LOG_FILE):
    try:
        with open(LOG_FILE, "r") as file:
            errors = [line.strip() for line in file if line.strip().startswith("ERROR")]

        if not errors:
            print("📭 No ERROR lines found.\n")
            return

        print("\n🚨 ERROR Lines:")
        for err in errors:
            print(err)
        print()
    except FileNotFoundError:
        print("❌ Log file not found. Please ensure sample.log exists.")
        
def show_menu():
    print("1. Analyze Log File")
    print("2. View All ERROR Lines")
    print("3. Exit\n")
    
def main():
    while True:
        show_menu()
        choice = input("Choose between (1-3): ")
        
        if choice == "1":
            total_lines = 0
            info_count = 0
            warning_count = 0
            error_count = 0
            analyze_log(LOG_FILE, total_lines, info_count, warning_count, error_count)
            
        elif choice == "2":
            view_errors(LOG_FILE)
            
        elif choice == "3":
            print("👋 Exiting Log File Analyzer. Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-3.\n")

if __name__ == "__main__":
    main()