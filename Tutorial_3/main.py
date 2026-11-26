# Tutorial 3 - cafe billing main program
from utils import calculate_total

# print the receipt for one customer
def print_receipt(name, coffee, tea, sandwich, total):
    print("\n==== RECEIPT ====")
    print(f"Customer : {name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("-----------------")
    print(f"Total = RM {total:.2f}")

def main():
    print("CAFE BILLING SYSTEM")
    name = input("Customer name: ")
    coffee = int(input("Coffee quantity: "))
    tea = int(input("Tea quantity: "))
    sandwich = int(input("Sandwich quantity: "))
    total = calculate_total(coffee, tea, sandwich)
    print_receipt(name, coffee, tea, sandwich, total)

if __name__ == "__main__":
    main()
