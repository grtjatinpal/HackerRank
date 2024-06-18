"""
Example
A = [1, 2]
B = [3, 4]
AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
"""

from itertools import product

# Solution 1: Using itertools.product
def _product(List1, List2):
    List_product = product(List1, List2)
    print(*List_product)  # Unpack the product and print each tuple separately

# Solution 2: Using nested loops
def _product_nested(List1, List2):
    List_product = []
    for element_List1 in List1:
        for element_List2 in List2:
            List_product.append((element_List1, element_List2))
    print(*List_product)  # Unpack the product and print each tuple separately
        

if __name__ == '__main__':
    List1 = list(map(int, input().split()))
    List2 = list(map(int, input().split()))
    _product(List1, List2)
    _product_nested(List1, List2)
