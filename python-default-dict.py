from collections import defaultdict


def find_words(n, m):

    d = defaultdict(list)

    for i in range(len(n)):
        d[n[i]].append(i + 1)


    for word in m:
        yield d.get(word, [-1])


def test_empty_list():
    """ returns empty list """
    group_a = []
    group_b = []

    assert list(find_words(group_a, group_b)) == []

def test_contains_all_one_group():
    """return all if all in one group"""
    group_a = ['a', 'a', 'a', 'a', 'a']
    group_b = ['a']

    assert list(find_words(group_a, group_b)) == [[1, 2, 3, 4, 5]]


def test():
    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a', 'b']
    assert list(find_words(group_a, group_b)) == [[1, 2, 4], [3, 5]]

    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['b', 'a']
    assert list(find_words(group_a, group_b)) == [[3, 5], [1, 2, 4]]

    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a', 'a']
    assert list(find_words(group_a, group_b)) == [[1, 2, 4], [1, 2, 4]]


def test_group_b_element_not_found():
    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a', 'b', 'c']

    assert list(find_words(group_a, group_b)) == [[1, 2, 4], [3, 5], [-1]]



def test_single_group():
    """returns all when one group specified"""
    group_a = ['a', 'a', 'b', 'a', 'b']
    group_b = ['a']

    assert list(find_words(group_a, group_b)) == [[1, 2, 4]]
