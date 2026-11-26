# Week 7 tutorial - FoodExpress order program (fixed)
from food_order import food_order

def main():
    # validate the customer input: the old version crashed here on letters
    try:
        price = float(input("Price (RM): "))
        quantity = int(input("Quantity: "))
    except ValueError:
        print("Invalid input. Price must be a number and quantity a whole number.")
        return

    total = food_order(price, quantity)
    if total == "invalid price" or total == "invalid quantity":
        print(total)
    else:
        print(f"Total Payment = RM {total:.2f}")

if __name__ == "__main__":
    main()
