from validation import checked, PositiveInteger


def simple_gcd(a, b):
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


@checked
def gcd(a: PositiveInteger, b: PositiveInteger):
    """Computes the greatest common divisor of a and b"""
    if a > b:
        return gcd(b, a)
    while b != 0:
        a, b = b, a % b
    return a


# To run in IPython: ipython -i func_perf.py
# %timeit gcd(27, 36) # 8.01 µs ± 268 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
# %timeit simple_gcd(27, 36) # 617 ns ± 42.1 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
