class Integer:
    @classmethod
    def check(cls, val):
        assert isinstance(val, int), "Expected int"


class Float:
    @classmethod
    def check(cls, val):
        assert isinstance(val, float), "Expected float"


class String:
    @classmethod
    def check(cls, val):
        assert isinstance(val, str), "Expected str"


class Positive:
    @classmethod
    def check(cls, val):
        assert val > 0, "Expected > 0"


class Nonempty:
    @classmethod
    def check(cls, val):
        assert len(val) > 0, "Expected non empty"


def gcd(a: int, b: int):
    """Computes the greatest common divisor of a and b"""
    Integer.check(a)
    Positive.check(a)
    Integer.check(b)
    Positive.check(b)
    if a > b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


def format(brand: str, price: float):
    String.check(brand)
    Nonempty.check(brand)
    Float.check(price)
    Positive.check(price)
    return f"{brand}: ${price:.2f}"


# print("gcd(27, 36) =", gcd(27, 36))
# print("gcd(2.7, 3.6) =", gcd(2.7, 3.6))
# print("gcd('27', '36') =", gcd('27', '36'))
# print("format('Apple', 123.4) =", )
