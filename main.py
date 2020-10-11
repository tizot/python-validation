def gcd(a: int, b: int):
    """Computes the greatest common divisor of a and b"""
    if a > b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


def format(brand: str, price: float):
    return f"{brand}: ${price:.2f}"


# print("gcd(27, 36) =", gcd(27, 36))
# print("gcd(2.7, 3.6) =", gcd(2.7, 3.6))
# print("gcd('27', '36') =", gcd('27', '36'))
# print("format('Apple', 123.4) =", )
