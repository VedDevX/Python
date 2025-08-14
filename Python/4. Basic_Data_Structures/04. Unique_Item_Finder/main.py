def add_item(items_set, item):
    """
    Add an item to the set.
    """
    item = item.strip()
    if not item:
        print("❌ Item cannot be empty.")
        return
    if item in items_set:
        print(f"⚠ '{item}' already exists.")
    else:
        items_set.add(item)
        print(f"✅ '{item}' added.")

def view_items(items_set):
    """
    Display all unique items.
    """
    if not items_set:
        print("📭 No items to display.")
        return
    print("📝 Unique Items:")
    for i, item in enumerate(sorted(items_set), start=1):
        print(f"{i}. {item}")

def search_item(items_set, item):
    """
    Check if an item exists in the set.
    """
    item = item.strip()
    if item in items_set:
        print(f"🔍 '{item}' exists in the collection.")
    else:
        print(f"❌ '{item}' not found.")

def remove_item(items_set, item):
    """
    Remove an item from the set.
    """
    item = item.strip()
    if item in items_set:
        items_set.remove(item)
        print(f"✅ '{item}' removed.")
    else:
        print(f"❌ '{item}' not found. Cannot remove.")

# ------------------------
# User Interface
# ------------------------

def show_menu():
    print("\n🎯 Unique Item Finder Menu")
    print("1. Add item")
    print("2. View all items")
    print("3. Search for an item")
    print("4. Remove an item")
    print("5. Exit")

def main():
    unique_items = set()  # In-memory set to store unique items

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            item = input("Enter item to add: ")
            add_item(unique_items, item)

        elif choice == "2":
            view_items(unique_items)

        elif choice == "3":
            item = input("Enter item to search: ")
            search_item(unique_items, item)

        elif choice == "4":
            item = input("Enter item to remove: ")
            remove_item(unique_items, item)

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1-5.")

if __name__ == "__main__":
    main()
