import time

class WishlistManager:
    def __init__(self):
        self.wishlist = []
        self.cart = []
        self.price_tracking = {}

    def add_to_wishlist(self, product):
        self.wishlist.append(product)
        print(f"{product} added to wishlist.")

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"{product} added to cart.")

    def track_price(self, product, target_price):
        self.price_tracking[product] = target_price
        print(f"Tracking price for {product}. Target price: ₹{target_price}")

    def check_price_drops(self):
        for product, target_price in self.price_tracking.items():
            current_price = self.get_current_price(product)
            if current_price < target_price:
                self.notify_price_drop(product, current_price)

    def get_current_price(self, product):
        # Mocked price retrieval for testing
        mock_prices = {
            "Smartwatch": 24000,  # Mock price in INR
            "Smartphone": 30000,  # Mock price in INR
            "Laptop": 60000,      # Mock price in INR
        }
        return mock_prices.get(product, float('inf'))  # Return a high value if product not found

    def notify_price_drop(self, product, current_price):
        print(f"Price drop alert! {product} is now ₹{current_price}.")

    def suggest_products(self):
        # Simulate product suggestions based on cart items
        suggestions = []
        for item in self.cart:
            suggestions.extend(self.get_suggestions_based_on(item))
        return suggestions

    def get_suggestions_based_on(self, item):
        # Simulate fetching suggestions
        return [f"Suggested product for {item}"]

# Example usage
if __name__ == "__main__":
    wishlist_manager = WishlistManager()
    wishlist_manager.add_to_wishlist("Smartwatch")
    wishlist_manager.add_to_cart("Smartphone")
    wishlist_manager.track_price("Smartwatch", 25000)  # Price in INR

    while True:
        wishlist_manager.check_price_drops()
        time.sleep(10)  # Check every 10 seconds for demonstration purposes
