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


def Reference(cls):
    """Dynamically creates subclass of Typed to reference classes"""
    return type(cls.__name__, (Typed, ), {"type": cls})


class Entity:
    @classmethod
    def __init_subclass__(cls):
        for name, attr in cls.__dict__.items():
            if callable(attr):
                setattr(cls, name, checked(attr))
        for name, ann in cls.__annotations__.items():
            if issubclass(ann, Contract):
                contract = ann()  # Integer()
            else:
                contract = Reference(ann)()  # instantiate dynamic Reference(Game)
            contract.__set_name__(cls, name)
            setattr(cls, name, contract)


@dataclass
class Game(Entity):
    name: NonemptyString


@dataclass
class Player(Entity):
    name: NonemptyString
    x: Integer
    y: Integer
    game: Game

    def left(self, dx: PositiveInteger):
        self.x -= dx

    def right(self, dx: PositiveInteger):
        self.x += dx

    def down(self, dy: PositiveInteger):
        self.y -= dy

    def up(self, dy: PositiveInteger):
        self.y += dy


game = Game("Super Mario Bros")
p = Player("Mario", 3, 4, game)
