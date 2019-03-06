import sys

d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

def assert_equal(tag, a, b):
    try:
        if a != b: raise AssertionError
    except Exception as exc:
        print(repr(exc))
        print("a:", a)
        print("b:", b)
    else:
        print(f"TEST {'[' + repr(tag) + ']':<12s} PASSED")


assert_equal("base1", {**d, **e}, {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'})
assert_equal("base2", {**e, **d}, {'cheese': 3, 'aardvark': 'Ethel', 'spam': 1, 'eggs': 2})

assert_equal("d + e", d + e, {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'})
assert_equal("e = d", e + d, {'cheese': 3, 'aardvark': 'Ethel', 'spam': 1, 'eggs': 2})

idd = id(d)
d += e
assert_equal("d += e", d, {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'})
assert_equal("id(d)", idd, id(d))

#===================================================================================================
d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}
d += e.items()
assert_equal("d += e", d, {'spam': 1, 'eggs': 2, 'cheese': 'cheddar', 'aardvark': 'Ethel'})

#===================================================================================================
d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

assert_equal("d - e", d - e, {'spam': 1, 'eggs': 2})
assert_equal("e - d", e - d, {'aardvark': 'Ethel'})

#===================================================================================================
d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

idd = id(d)
d -= e
assert_equal("d -= e", d, {'spam': 1, 'eggs': 2})
assert_equal("id(d)", idd, id(d))

#===================================================================================================
d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

ide = id(e)
e -= d
assert_equal("e -= d", e, {'aardvark': 'Ethel'})
assert_equal("id(e)", ide, id(e))

#===================================================================================================
d = {'spam': 1, 'eggs': 2, 'cheese': 3}
e = {'cheese': 'cheddar', 'aardvark': 'Ethel'}

e -= d.items()
assert_equal("e -= d", e, {'aardvark': 'Ethel'})


a = {'a':'a', 'b':'b'}
A = {'b':'B', 'c':'C'}

# Raise at the last minute to prevent the module from being cached.
raise RuntimeError("All tests complete.")