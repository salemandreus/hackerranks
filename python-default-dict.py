from collections import defaultdict


def find_words(arr1, arr2):

    a = defaultdict(int)
    b = defaultdict(int)

    for i in range(len(arr1)):
        if i == 'a':
            a[arr1[i]] = i
        elif i == 'b':
            b[arr1[i]] = i
    return a


def test():
    arr1 = ['a', 'a', 'b', 'a', 'b']
    arr2 = ['a', 'b']

    assert find_words(arr1, arr2) == [1, 2, 4], [3, 5]

    #
    # for i in range(m+n):
    #     if n < i < m:
    #         if n < i < m:

def test_fail():
    assert False

def test_null():
    assert False