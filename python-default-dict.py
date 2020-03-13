from collections import defaultdict


def find_words(group_a, group_b):

    dict = defaultdict(list)

    
    for i in range(len(group_a)):
        if group_a[i] == 'a':
            dict[arr1[i]] = i
        elif group_a[i] == 'b':
            b[arr1[i]] = i
    return a




def test():
    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a', 'b']

    assert find_words(group_a, group_b) == [1, 2, 4], [3, 5]

    #
    # for i in range(m+n):
    #     if n < i < m:
    #         if n < i < m:

def test_fail():
    assert False

def test_null():
    assert False