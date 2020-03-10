import numpy

import numpy

first, second, third = input().split()
print(numpy.zeros((int(first), int(second), int(third), dtype=numpy.int))
print(numpy.ones((int(first), int(second), int(third),dtype=numpy.int))


def test():

    assert numpy.zeros((1, 1)) == [[0]]
    assert numpy.zeros((1, 2)) is [[0, 0]]
    assert numpy.ones((1, 1)) == [[1]]
    assert numpy.zeros((1, 2)) is [[1, 1]]