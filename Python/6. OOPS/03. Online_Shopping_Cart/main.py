class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stcok = stock
        
    def display_product(self):
        print(f"{self.name} - ₹{self.price} ({self.stock} available)")
        
class ShoppingCart(Product):
    def __init__(self):
        self.items = {}
        
    def add_items(self, product, quantity):
        if quantity > product.stock:
            print(f"❌ Only {product.stock} units available for {product.name}.")
        elif quantity <= 0:
            print("❌ Quantity must be positive.")
        else:
            product.stock -= quantity
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
            print(f"✅ Added {quantity} x {product.name} to cart.")
            
    def remove_item(self, product_name):
        if product_name in self.items:
            removed_product = self.items.pop(product_name)
            removed_product['product'].stock += removed_product['quantity']
            print(f"🗑 Removed {product_name} from cart.")
        else:
            print("❌ Item not found in cart.")

    def view_cart(self):
        if not self.items:
            print("📭 Your cart is empty.")
            return
        print("\n🛒 Your Cart:")
        for name, info in self.items.items():
            print(f"{name} - {info['quantity']} units - ₹{info['product'].price} each")
        total = sum(info['quantity'] * info['product'].price for info in self.items.values())
        print(f"💰 Total: ₹{total}")

    def checkout(self):
        if not self.items:
            print("📭 Your cart is empty.")
            return
        total = sum(info['quantity'] * info['product'].price for info in self.items.values())
        print(f"\n✅ Checkout Complete! Total amount: ₹{total}")
        self.items.clear()


# ------------------ MENU ------------------

def show_menu():
    print("\n===== 🛍 Online Shopping Menu =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout & Exit")


def main():
    # Sample products
    products = [
        Product("T-Shirt", 499, 10),
        Product("Jeans", 999, 5),
        Product("Sneakers", 2499, 3),
        Product("Cap", 299, 7)
    ]

    cart = ShoppingCart()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            print("\n🛒 Available Products:")
            for prod in products:
                prod.display_product()

        elif choice == "2":
            product_name = input("Enter product name to add: ")
            quantity = int(input("Enter quantity: "))
            found = False
            for prod in products:
                if prod.name.lower() == product_name.lower():
                    cart.add_item(prod, quantity)
                    found = True
                    break
            if not found:
                print("❌ Product not found.")

        elif choice == "3":
            product_name = input("Enter product name to remove: ")
            cart.remove_item(product_name)

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            cart.checkout()
            print("👋 Thank you for shopping! Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()