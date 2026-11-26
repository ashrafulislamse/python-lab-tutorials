# Tutorial 3 - logic functions for the cafe bill

# item prices in RM
PRICE_COFFEE = 8.50
PRICE_TEA = 6.00
PRICE_SANDWICH = 12.00

# calculate the total bill from the quantity of each item
def calculate_total(coffee, tea, sandwich):
    total = (coffee * PRICE_COFFEE) + (tea * PRICE_TEA) + (sandwich * PRICE_SANDWICH)
    return total
