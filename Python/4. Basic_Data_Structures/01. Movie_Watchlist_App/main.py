def normalize_title(title):
    title.strip().lower()
    
def validate_year(year_str):
    year = int(year_str)
    if year < 0:
        raise ValueError("Year must be positive.")
    return year

def add_movie(movies, title, year_str):
    try:
        year = validate_year(year_str)
    except ValueError:
        print("❌ Invalid year. Please enter a positive number.")
        return False

    if not title.strip():
        print("❌ Title cannot be empty.")
        return False
    
    if any(normalize_title(m["title"]) == normalize_title(title) and m["year"] == year for m in movies):
        print("⚠ Movie already exists in watchlist.")
        return False
    
    movies.append({"title": title.strip(), "year": year, "watched": False})
    print(f"'{title.strip()}'- ({year}) added to watchlist")
    
def list_movies(movies, only_watched=None):
    filtered = movies
    
    if only_watched is True:
        filtered = [m for m in movies if m["watched"]]
    elif only_watched is False:
        filtered = [m for m in movies if not m["watched"]]

    if not filtered:
        print("📭 No movies to display.")
        return
    
    for idx, movie in enumerate(movies, start=1):
        print(f"{idx}.{movie['title']} ({movie['year']}) - {'Watched' if movie['watched'] else 'Not Watched'}")
        
def find_movie(movies, identifier):
    if identifier.isdigit():
        idx = int(identifier) - 1
        if 0 <= idx < len(movies):
            return movies[idx]
        
    for movie in movies:
        if normalize_title(movie["title"]) == normalize_title(identifier):
            return movie
    
    return None

def mark_watched(movies, identifier):
    movie = find_movie(movies, identifier)
    if movie:
        movie["watched"] = True
        print(f"✅ '{movie['title']}' marked as watched.")
    else:
        print("❌ Movie not found.")
        
def remove_movie(movies, identifier):
    movie = find_movie(movies, identifier)
    if movie:
        movies.remove(movie)
        print(f"🗑 Removed '{movie['title']}' from watchlist.")
    else:
        print("❌ Movie not found.")
        
def show_menu():
    print("\n🎬 Movie Watchlist Menu")
    print("1. Add movie")
    print("2. View watchlist")
    print("3. Mark as watched")
    print("4. Remove movie")
    print("5. Exit")
    
def main():
    movies = []
    
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            title = input("Enter movie title: ")
            year = input("Enter movie year: ")
            add_movie(movies, title, year)
            
        elif choice == "2":
            list_movies(movies)
            
        elif choice == "3":
            identifier = input("Enter movie title or index to mark as watched: ")
            mark_watched(movies, identifier)
            
        elif choice == "4":
            identifier = input("Enter movie title or index to remove: ")
            remove_movie(movies, identifier)
            
        elif choice == "5":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Enter a number from 1-6.")
            
if __name__ == "__main__":
    main()