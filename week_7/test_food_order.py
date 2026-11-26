# Week 7 tutorial - pytest checks for food_order
from food_order import food_order

def test_order1():
    assert food_order(10, 2) == 20

# test if total food order is equal to 30
# test if total food order is equal to 100
# test if total food order is equal to 10
def test_order2():
    assert food_order(10, 3) == 30
    assert food_order(50, 2) == 100
    assert food_order(10, 1) == 10

# test if total food order is equal to "invalid price"
def test_invalid_price():
    assert food_order(-5, 2) == "invalid price"

# test if total food order is equal to "invalid quantity"
def test_invalid_quantity():
    assert food_order(10, 0) == "invalid quantity"
