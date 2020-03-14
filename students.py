from textwrap import dedent



def append_item_to_list(n, s):
    students.append([n, s])

    return students

def get_second_lowest(st):
    return st


def test_append_item_to_list_single():
    lines =dedent("""
    Harry 37.21
    """).splitlines()

    assert append_item_to_list(lines) == 5

def test_append_item_to_list_multiple():
    lines =dedent("""
    Harry 37.21
    Berry 37.21
    Tina 37.2
    Akriti 41
    Harsh 39
    """).splitlines()

    assert append_item_to_list(lines) == 5




if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        # stud = append_item_to_list(name, score)
        print(get_second_lowest(stud))

