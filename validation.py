from collections import ChainMap
from functools import wraps
from inspect import signature


_contracts = {}

class Contract:
    @classmethod
    def __init_subclass__(cls):
        # register contract
        _contracts[cls.__name__] = cls

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


def _get_contract_cls(ann):
    if issubclass(ann, Contract):
        return ann  # Integer
    else:
        return Reference(ann)  # dynamic Reference(SomeClass)


def checked(func):
    sig = signature(func)
    ann = func.__annotations__
    @wraps(func)
    def wrapped(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            if name in ann:
                _get_contract_cls(ann[name]).check(val)
        return func(*args, **kwargs)
    return wrapped


def Reference(cls):
    """Dynamically creates subclass of Typed to reference classes"""
    return type(cls.__name__, (Typed, ), {"type": cls})


class EntityMeta(type):
    @classmethod
    def __prepare__(cls, *args):
        return ChainMap({}, _contracts)

    def __new__(cls, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(cls, name, bases, methods)


class Entity(metaclass=EntityMeta):
    @classmethod
    def __init_subclass__(cls):
        for name, attr in cls.__dict__.items():
            if callable(attr):
                setattr(cls, name, checked(attr))
        for name, ann in cls.__annotations__.items():
            contract = _get_contract_cls(ann)()
            contract.__set_name__(cls, name)
            setattr(cls, name, contract)
