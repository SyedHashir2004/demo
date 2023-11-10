def multiply(a, b):
    """
    Multiply two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The product of a and b.
    """
    result = a * b
    return result

if __name__ == "__main__":
    a = 1
    b = 2
    product = multiply(a, b)
    print(f"The product of {a} and {b} is {product}")
