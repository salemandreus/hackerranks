from collections import defaultdict


def find_words(n, m):

    d = defaultdict(list)

    for i in range(len(n)):
        for word in m:
            if n[i] == word:
                d[word].append(i + 1)

    return list(d.values())

def test_empty_list():
    """ returns empty list """
    group_a = []
    group_b = []

    assert find_words(group_a, group_b) == []

def test_contains_all_one_group():
    """return all if all in one group"""
    group_a = ['a', 'a', 'a', 'a', 'a']
    group_b = ['a']

    assert find_words(group_a, group_b) == [[1, 2, 3, 4, 5]]


def test_single_group():
    """returns all when one group specified"""
    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a']

    assert find_words(group_a, group_b) == [[1, 2, 4]]


def test():
    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a', 'b']

    assert find_words(group_a, group_b) == [[1, 2, 4], [3, 5]]


def test_group_b_element_not_found():
    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a', 'b', 'c']

    assert find_words(group_a, group_b) == [[1, 2, 4], [3, 5], [-1]]

