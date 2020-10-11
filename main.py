from dataclasses import dataclass
from functools import wraps
from inspect import signature


class Contract:
    # called on "owner" creation
    def __set_name__(self, owner, name):
        self.name = name

    # this makes Contract a (data) descriptor
    def __set__(self, instance, val):
        self.check(val)
        instance.__dict__[self.name] = val

    @classmethod
    def check(cls, val): ...


class Typed(Contract):
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


class Positive(Contract):
    @classmethod
    def check(cls, val):
        assert val > 0, "Expected > 0"
        super().check(val)


class Nonempty(Contract):
    @classmethod
    def check(cls, val):
        assert len(val) > 0, "Expected non empty"
        super().check(val)


class PositiveInteger(Integer, Positive): ...
class PositiveFloat(Float, Positive): ...
class NonemptyString(String, Nonempty): ...


def checked(func):
    sig = signature(func)
    ann = func.__annotations__
    @wraps(func)
    def wrapped(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in ann:
                ann[name].check(val)
        return func(*args, **kwargs)
    return wrapped


@checked
def gcd(a: PositiveInteger, b: PositiveInteger):
    """Computes the greatest common divisor of a and b"""
    if a > b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


@checked
def format(brand: NonemptyString, price: PositiveFloat):
    return f"{brand}: ${price:.2f}"


@dataclass
class Player:
    name: str = NonemptyString()
    x: int = Integer()
    y: int = Integer()

    def left(self, dx):
        self.x -= dx

    def right(self, dx):
        self.x += dx

    def down(self, dy):
        self.y -= dy

    def up(self, dy):
        self.y += dy


p = Player("Mario", 3, 4)
