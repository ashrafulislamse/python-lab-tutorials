# Week 7 tutorial - FoodExpress order logic (debugged version)
# The tests call food_order(price, quantity), so the final function keeps
# that name and returns one value: the total, or an error message string.

def food_order(price, quantity):
    if price <= 0:
        return "invalid price"
    if quantity <= 0:
        return "invalid quantity"
    return price * quantity
