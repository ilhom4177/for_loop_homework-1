def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    list1=[]
    x=0
    for i in range(1,11):
        x=x+price
        list1.append(x)
    return list1