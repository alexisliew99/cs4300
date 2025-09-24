# Create file name task4.py that defines a function calculate_discount which computes
# the final price of a product after applying a discount. The function accept any numeric 
# type (integer or float) for both price and discount. Also, write pytest test cases to verify 
# calculate_discount with different numeric types.

def calculate_discount(price, discount):
    if not (isinstance(price, (int, float)) and isinstance(discount, (int, float))):
        raise TypeError("Price and discount must be numeric")
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount / 100)
