def sockMerchant(n, ar):

    set_socks = set(ar)

    pairs = 0
    for j in set_socks:
        pairs += (ar.count(j) // 2)

    # return "List:" + str(ar) + "\nSet:" + str(set_socks) + "\nPairs: " + str(pairs)
    return pairs

# def identify_pairs():
#
#
# def test_identify_pairs():
#     ar = [1, 2, 1, 2, 1, 3, 2]
#     assert list(identify_pairs(9, ar)) == 2


def test_sockMerchant_1():

    ar = [1, 2, 1, 2, 1, 3, 2]
    assert sockMerchant(7, ar) == 2


def test_sockMerchant_2():

    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    assert sockMerchant(9, ar) == 3


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()



