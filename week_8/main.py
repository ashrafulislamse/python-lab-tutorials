# Week 8 - food delivery receipt generator (main program)
import customer
import receipt

def main():
    # getting the customer data from the customer module
    name, food, quantity, price, delivery_charges = customer.get_customer()
    # print the food receipt with the receipt module
    receipt.print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()
