class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"📖 {self.title} by {self.author} (ISBN: {self.isbn}) - {status}")


class Library(Book):
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        print(f"✅ Book '{book.title}' added successfully!")
        
    def remove_book(self, isbn):
        for book in self.book:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"🗑 Book '{book.title}' removed successfully!")
                return
        print("❌ Book not found!")
        
        
    def search_book(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                book.display_info()
                found = True
        if not found:
            print("📭 No matching books found.")
            
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"📕 You borrowed '{book.title}' successfully!")
                else:
                    print("⚠ Sorry, this book is already borrowed.")
            return
        print("❌ Book not found!")
        
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"📗 Book '{book.title}' returned successfully!")
                else:
                    print("⚠ This book was not borrowed.")
            return
        print("❌ Book not found!")
        
    def display_books(self):
        if not self.books:
            print("📭 No books available in the library.")
            return
        print("\n📚 Library Books:")
        for book in self.books:
            book.display_info()
            
            
def show_menu():
    print("\n===== 📚 Library Menu =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Display All Books")
    print("7. Exit")
    
def main():
    library = Library()
    
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            new_book = Book(title, author, isbn)
            library.add_book(new_book)
            
        elif choice == "2":
            isbn = input("Enter ISBN of book to remove: ")
            library.remove_book(isbn)

        elif choice == "3":
            keyword = input("Enter book title/author to search: ")
            library.search_book(keyword)

        elif choice == "4":
            isbn = input("Enter ISBN of book to borrow: ")
            library.borrow_book(isbn)

        elif choice == "5":
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(isbn)

        elif choice == "6":
            library.display_books()

        elif choice == "7":
            print("👋 Exiting Library Management System. Goodbye!")
            break

        else:
            print("❌ Invalid choice! Please select between (1-7).")


if __name__ == "__main__":
    main()