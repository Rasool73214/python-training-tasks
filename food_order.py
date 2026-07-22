class food_order:
    def __init__(self, order_id, customer_name, items, total_amount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount

    def display_order(self):
        print(f"Order ID: {self.order_id}")
class Customer_login:        
    def __init__(self, username, password):
        self.username = username
        self.password = password
        if self.username == "rasool" and self.password == "12345":
            print("Login successful")
        else:
            print("Login failed")
class place_order(food_order):
    def __init__(self, order_id, customer_name, items, total_amount, quantity):
        super().__init__(order_id, customer_name, items, total_amount)
        self.quantity = quantity
        self.total_amount = total_amount * quantity

        if quantity > 0:
            print("product is available")
            print("order placed successfully")
        else:
            print("out of stock")

        print("total amount:", self.total_amount)

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Items: {self.items}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Amount: {self.total_amount}")


class order_history(food_order):
    def __init__(self, order_id, customer_name, items, total_amount):
        super().__init__(order_id, customer_name, items, total_amount)

    def display_history(self):
        print("order history displayed successfully")
        print("order id:", self.order_id)
        print("customer name:", self.customer_name)
        print("items:", self.items)
        print("total amount:", self.total_amount)


if __name__ == "__main__":
    username = input("Enter username: ")
    password = input("Enter password: ")
    login = Customer_login(username, password)

    if username == "rasool" and password == "12345":
        order_id = input("Enter order ID: ")
        customer_name = input("Enter customer name: ")
        items_input = input("Enter food items (comma-separated): ")
        items = [item.strip() for item in items_input.split(",") if item.strip()]
        total_amount = float(input("Enter price per item: "))
        quantity = int(input("Enter quantity: "))

        order = place_order(order_id, customer_name, items, total_amount, quantity)
        print("\nOrder details:")
        order.display_order()

        history = order_history(order_id, customer_name, items, order.total_amount)
        print("\nOrder history:")
        history.display_history()
    else:
        print("Cannot place order without successful login.")