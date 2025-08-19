import numpy as np

# Sample stock prices (you can modify or even take user input)
prices = np.array([100, 102, 98, 105, 110, 108, 112, 115, 117, 120])

def show_menu():
    print("\n📊 Stock Market Data Analysis")
    print("1. View Stock Prices")
    print("2. Show Basic Statistics (Avg, Max, Min, Volatility)")
    print("3. Show Daily Returns (%)")
    print("4. Show 3-Day Moving Average")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        print("\n📈 Stock Prices:", prices)

    elif choice == "2":
        print("\n📊 Basic Statistics")
        print("Average Price:", np.mean(prices))
        print("Highest Price:", np.max(prices))
        print("Lowest Price:", np.min(prices))
        print("Volatility (Std Dev):", round(np.std(prices), 2))

    elif choice == "3":
        daily_returns = (np.diff(prices) / prices[:-1]) * 100
        print("\n💹 Daily Returns (%):")
        print(daily_returns)

    elif choice == "4":
        moving_avg = np.convolve(prices, np.ones(3)/3, mode='valid')
        print("\n📉 3-Day Moving Average:")
        print(moving_avg)

    elif choice == "5":
        print("👋 Exiting Stock Market Analysis. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter 1-5.")
