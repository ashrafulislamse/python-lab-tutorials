# Tutorial 3 (Week 5) - Cafe Billing Program

## 1. Answers to the Questions

### 1.1 Problem Statement

A small cafe sells Coffee at RM 8.50, Tea at RM 6.00 and Sandwiches at RM 12.00. The cashier currently calculates every bill by hand, which is slow and easy to get wrong when a customer orders several items. Build a Python program that asks for the customer's order, calculates the bill automatically and prints a neat receipt.

### 1.2 What are the Inputs?

| Input | Type | Example |
|---|---|---|
| Customer name | text | Bobby |
| Coffee quantity | whole number | 3 |
| Tea quantity | whole number | 3 |
| Sandwich quantity | whole number | 2 |

### 1.3 What are the Outputs?

| Output | Type | Example |
|---|---|---|
| Receipt with the customer name and each quantity | text | see sample below |
| Total bill in Ringgit Malaysia | number, 2 decimal places | RM 67.50 |

### 1.4 What Would Be the Typical Process Flow?

1. The cashier enters the customer name
2. The cashier enters the quantity for each item
3. `utils.calculate_total()` multiplies each quantity by its price and adds the three amounts
4. The total is sent back to `main.py`
5. `print_receipt()` prints the receipt with the name, quantities and total

### 1.5 What Are the Constraints?

- Quantities must be whole numbers of 1 or more (you cannot order half a sandwich)
- Prices are fixed by the cafe, so the program keeps them as constants and does not ask for them
- The total is displayed with 2 decimal places, following money format
- The cafe has only these three items, so no other products are handled

## 2. How Do You Decompose the Problem into Smaller Tasks?

The problem splits into two responsibilities, one file each:

| Task | File | Function |
|---|---|---|
| Calculation logic: turn quantities into a total | `utils.py` | `calculate_total(coffee, tea, sandwich)` |
| Input and display: read the order and print the receipt | `main.py` | `print_receipt(name, coffee, tea, sandwich, total)` and `main()` |

Splitting the problem this way keeps the calculation separate from the input and output. If the cafe changes a price, only `utils.py` changes. If the receipt layout changes, only `main.py` changes. Each function has one job, which makes testing and fixing simpler.

## 3. Pseudocode

```
START
    PRINT "CAFE BILLING SYSTEM"
    READ name
    READ coffee_quantity
    READ tea_quantity
    READ sandwich_quantity

    total = (coffee_quantity * 8.50) + (tea_quantity * 6.00) + (sandwich_quantity * 12.00)

    PRINT "==== RECEIPT ===="
    PRINT name
    PRINT coffee_quantity, tea_quantity, sandwich_quantity
    PRINT "-----------------"
    PRINT "Total = RM ", total (2 decimal places)
END
```

## 4. The Code

### Challenge 1: Logic Functions in utils.py

`utils.py` holds the three prices as constants and one calculation function:

```python
PRICE_COFFEE = 8.50
PRICE_TEA = 6.00
PRICE_SANDWICH = 12.00

def calculate_total(coffee, tea, sandwich):
    total = (coffee * PRICE_COFFEE) + (tea * PRICE_TEA) + (sandwich * PRICE_SANDWICH)
    return total
```

The function receives three quantities, multiplies each one by its price, adds the three amounts and returns one total. It does no input and no printing, so it can be reused by any other program that needs the cafe's prices.

### Challenge 2: Main Program in main.py

`main.py` imports the calculation from `utils`, reads the order and prints the receipt:

```python
from utils import calculate_total

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
```

`print_receipt()` takes five parameters: the name, the three quantities and the calculated total. `main()` reads the inputs, calls the logic function for the total, then hands everything to `print_receipt()`.

## Sample Run

Input: name Bobby, coffee 3, tea 3, sandwich 2.

```
==== RECEIPT ====
Customer : Bobby
Coffee   : 3
Tea      : 3
Sandwich : 2
-----------------
Total = RM 67.50
```

Check by hand: (3 x 8.50) + (3 x 6.00) + (2 x 12.00) = 25.50 + 18.00 + 24.00 = RM 67.50, which matches the program output.

## How to Run

```
python main.py
```

Both files must stay in the same folder because `main.py` imports the function from `utils.py`.
