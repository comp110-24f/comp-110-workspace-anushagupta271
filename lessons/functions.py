"""Practice functions"""

# from random import randint

# print(randint(3, 17))


# # Function Definition
# def sum(num1: int, num2: int) -> int:
#     """Return the sum of num1 and num2"""
#     return num1 + num2


# # Function Call
# print(sum(num1=randint(1, 2), num2=randint(0, 1)))  # <- arguments


# def total_cost(price: int, tax_rate: float):
#     print(price + (price * tax_rate))


# print(total_cost(price=100, tax_rate=0.07))


def total_cost(price: int, tax_rate: float):
    return price + (price * tax_rate)


print(total_cost(price=100, tax_rate=0.07))
