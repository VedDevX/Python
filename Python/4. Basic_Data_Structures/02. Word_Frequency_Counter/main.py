import string

def normalize_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    return words

def count_words(text):
    words = normalize_text(text)
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def view_all(word_freq):
    if not word_freq:
        print("📭 No words to display.")
        return
    for word in sorted(word_freq.keys()):
        print(f"{word}: {word_freq[word]}")
        
def search_word(word_freq, word):
    word = word.lower()
    count = word_freq.get(word, 0)
    print(f"'{word}' appears {count} time(s).")
    
def top_n_words(word_freq, n):
    if not word_freq:
        print("📭 No words to display.")
        return
    
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    print(f"Top {n} words:")
    for i, (word, count) in enumerate(sorted_words[:n], start=1):
        print(f"{i}. {word}: {count}")
        
def show_menu():
    print("\n📊 Word Frequency Counter Menu")
    print("1. Input text and count words")
    print("2. View all word frequencies")
    print("3. Search for a word")
    print("4. View top N frequent words")
    print("5. Exit")

def main():
    word_freq = {}
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            text = input("Enter your text:\n")
            word_freq = count_words(text)
            print("✅ Words counted successfully!")

        elif choice == "2":
            view_all(word_freq)

        elif choice == "3":
            word = input("Enter word to search: ")
            search_word(word_freq, word)

        elif choice == "4":
            try:
                n = int(input("Enter N (number of top words to display): "))
                if n <= 0:
                    print("❌ N must be positive.")
                else:
                    top_n_words(word_freq, n)
            except ValueError:
                print("❌ Invalid input. Enter a positive integer.")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Enter a number from 1-5.")

if __name__ == "__main__":
    main()