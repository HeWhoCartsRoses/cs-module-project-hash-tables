"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
from itertools import permutations
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here


def test(var):
    q = []
    for i in var:
        q.append(f(i))
    x = list(permutations(q))
    y = []
    for l in x:
        z = list(l)
        add = z[0]+z[1]
        sub = z[2]-z[3]
        if add == sub:
            y.append(z)
    return y


if __name__ == "__main__":
    print(test(q))
