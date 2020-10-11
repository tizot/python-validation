class Constraint:
    @classmethod
    def check(cls, val): ...


class Typed(Constraint):
    type = None

    @classmethod
    def check(cls, val):
        assert isinstance(val, cls.type), f"Expected {cls.type}"
        super().check(val)


class Integer(Typed):
    type = int


class Float(Typed):
    type = float


class String(Typed):
    type = str


class Positive(Constraint):
    @classmethod
    def check(cls, val):
        assert val > 0, "Expected > 0"
        super().check(val)


class Nonempty(Constraint):
    @classmethod
    def check(cls, val):
        assert len(val) > 0, "Expected non empty"
        super().check(val)


class PositiveInteger(Integer, Positive): ...
class PositiveFloat(Float, Positive): ...
class NonemptyString(String, Nonempty): ...


def gcd(a: int, b: int):
    """Computes the greatest common divisor of a and b"""
    PositiveInteger.check(a)
    PositiveInteger.check(b)
    if a > b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


def format(brand: str, price: float):
    NonemptyString.check(brand)
    PositiveFloat.check(price)
    return f"{brand}: ${price:.2f}"


# print("gcd(27, 36) =", gcd(27, 36))
# print("gcd(2.7, 3.6) =", gcd(2.7, 3.6))
# print("gcd('27', '36') =", gcd('27', '36'))
# print("format('Apple', 123.4) =", )
