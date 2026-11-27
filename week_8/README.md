# Food Delivery Receipt Generator

A backend receipt generator for a Food Delivery System, built as a multi-module Python application for the Week 8 tutorial.

## 4.1 Purpose of the Application

The application calculates and prints a receipt for a food delivery order. The customer module collects the order, the receipt module calculates the subtotal, the 5 percent service charge, the delivery charge and the grand total, and prints a formatted receipt on the console. Splitting the work into modules follows industry practice: each module has one responsibility, so a change to the receipt layout never touches the customer input logic and the other way round.

## 4.2 Tech Stack

| Part | Choice |
|---|---|
| Language | Python 3 |
| External libraries | none, standard library only |
| Modules | `main.py` (entry point), `customer.py` (input), `receipt.py` (calculation and printing) |
| Platform | console / command line |

## 4.3 How to Use

Run the program from this folder:

```
python main.py
```

Then answer the prompts:

| Prompt | Example |
|---|---|
| Customer Name | izzad |
| Food Ordered (Cake/Muffin) | Cake |
| Quantity | 2 |
| Price per Item (RM) | 3.00 |
| Delivery (Y/N) | Y |

The program then prints the receipt. Answering N to the delivery question sets the delivery charge to RM 0.00.

### Module Structure

```
week_8/
├── main.py       # entry point: imports both modules and connects them
├── customer.py   # get_customer(): reads the order and the delivery choice
├── receipt.py    # print_receipt(): calculates and prints the receipt
└── README.md
```

### How the Charges Are Calculated

```
subtotal       = price x quantity
service charge = subtotal x 0.05
grand total    = subtotal + service charge + delivery charge
```

The delivery charge is RM 5.00 for delivery (Y) and RM 0.00 for self pickup (N).

### Sample Receipt

```
=== Customer Information ===
Customer Name : izzad
Food Ordered (Cake/Muffin) : Cake
Quantity : 2
Price per Item (RM): 3.00
Delivery (Y/N): Y

========== RECEIPT ==========
Customer  : izzad
Food      : Cake
Quantity  : 2
Price     : RM 3.00
----------------------------
Subtotal        : RM 6.00
Service Charge (5%) : RM 0.30
Delivery Charge : RM 5.00
----------------------------
TOTAL     : RM 11.30
=============================
```

## 4.4 Demonstration

![Week 8 receipt demo](demo.mp4)

The recording shows one delivery order (Y, total RM 11.30) and one self pickup order (N, total RM 6.30).
