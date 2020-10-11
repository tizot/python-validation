def gcd(a: int, b: int):
    """Computes the greatest common divisor of a and b"""
    assert isinstance(a, int), "Expected int"
    assert a > 0, "Expected > 0"
    assert isinstance(b, int), "Expected int"
    assert b > 0, "Expected > 0"
    if a > b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


def format(brand: str, price: float):
    assert isinstance(brand, str), "Expected str"
    assert len(brand) > 0, "Expected non empty"
    assert isinstance(price, float), "Expected float"
    assert price > 0, "Expected > 0"
    return f"{brand}: ${price:.2f}"


# print("gcd(27, 36) =", gcd(27, 36))
# print("gcd(2.7, 3.6) =", gcd(2.7, 3.6))
# print("gcd('27', '36') =", gcd('27', '36'))
# print("format('Apple', 123.4) =", )
