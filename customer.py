class Customer:
    def __init__(self, customer_name, phone):
        self.name = customer_name
        self.phone = phone

    def display_customer_name(self):
        print("Customer Name:", self.name)


class Order(Customer):
    def __init__(self, customer_name, phone, order_id, order_date, order_items):
        super().__init__(customer_name, phone)
        self.order_id = order_id
        self.order_date = order_date
        self.order_items = order_items

    def display_order(self):
        print("Order ID:", self.order_id)
        print("Order Date:", self.order_date)
        print("Order Items:", self.order_items)
        print("Customer Name:", self.name)
        print("Phone Number:", self.phone)


class Total(Order):
    def __init__(self, customer_name, phone, order_id, order_date, order_items, total_amount):
        super().__init__(customer_name, phone, order_id, order_date, order_items)
        self.total_amount = total_amount

    def display_total(self):
        print("Total Amount:", self.total_amount)
        print("Order ID:", self.order_id)
        print("Order Date:", self.order_date)
        print("Order Items:", self.order_items)
        print("Customer Name:", self.name)
        print("Phone Number:", self.phone)


class Payment(Total):
    def __init__(self, customer_name, phone, order_id, order_date, order_items, total_amount, payment_method):
        super().__init__(customer_name, phone, order_id, order_date, order_items, total_amount)
        self.payment_method = payment_method

        if total_amount > 0:
            print("payment successful")
        else:
            print("payment failed")

    def display_payment(self):
        print("Payment Method:", self.payment_method)
        self.display_total()


if __name__ == "__main__":
    customer_name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    order_id = input("Enter order ID: ")
    order_date = input("Enter order date: ")
    items_input = input("Enter order items (comma-separated): ")
    order_items = [item.strip() for item in items_input.split(",") if item.strip()]
    total_amount = float(input("Enter total amount: "))
    payment_method = input("Enter payment method: ")

    payment = Payment(
        customer_name,
        phone,
        order_id,
        order_date,
        order_items,
        total_amount,
        payment_method,
    )

    print("\nOrder details:")
    payment.display_payment()

                                 