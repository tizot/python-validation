from dataclasses import dataclass

from validation import Entity

# To run in IPython: ipython -i cls_perf.py

%%timeit # 463 µs ± 5.72 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
@dataclass
class Player:
    name: str
    x: int
    y: int

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        assert isinstance(val, str), "Expected str"
        assert len(val) > 0, "Expected non empty"
        self._name = val

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        assert isinstance(val, int), "Expected int"
        assert val > 0, "Expected > 0"
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        assert isinstance(val, int), "Expected int"
        assert val > 0, "Expected > 0"
        self._y = val

    def left(self, dx):
        self.x -= dx

    def right(self, dx):
        self.x += dx

    def down(self, dy):
        self.y -= dy

    def up(self, dy):
        self.y += dy

p = Player("Mario", 3, 4)
%timeit p.x # 162 ns ± 39 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
%timeit p.x = 5 # 332 ns ± 21.9 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

%%timeit # 733 µs ± 149 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
@dataclass
class Player(Entity):
    name: NonemptyString
    x: Integer
    y: Integer

    def left(self, dx):
        self.x -= dx

    def right(self, dx):
        self.x += dx

    def down(self, dy):
        self.y -= dy

    def up(self, dy):
        self.y += dy

p = Player("Mario", 3, 4)
%timeit p.x # 59.2 ns ± 0.461 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
%timeit p.x = 5 # 1.04 µs ± 144 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
