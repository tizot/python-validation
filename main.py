from dataclasses import dataclass
from validation import Entity, checked


# @checked
# def gcd(a: PositiveInteger, b: PositiveInteger):
#     """Computes the greatest common divisor of a and b"""
#     if a > b:
#         return gcd(b, a)
#     while b != 0:
#         a, b = b, a % b
#     return a


# @checked
# def format(brand: NonemptyString, price: PositiveFloat):
#     return f"{brand}: ${price:.2f}"


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
