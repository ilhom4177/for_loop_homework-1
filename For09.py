def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    s = [price]
    for i in range(9):
        s.append(s[-1] + 2.25)
    return s