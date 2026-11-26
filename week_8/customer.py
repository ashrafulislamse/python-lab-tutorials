# Week 8 - customer module: reads the customer's order
def get_customer():
    print("=== Customer Information ===")
    name = input("Customer Name : ")
    food = input("Food Ordered (Cake/Muffin) : ")
    quantity = int(input("Quantity : "))
    price = float(input("Price per Item (RM): "))
    delivery = input("Delivery (Y/N): ")
    # if-else decides the delivery charge
    if delivery == "Y" or delivery == "y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00
    return name, food, quantity, price, delivery_charges
