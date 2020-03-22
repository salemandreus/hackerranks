from textwrap import dedent


def get_second_lowest(lines):
    marks = set()
    for line in lines:
        student, mark = line.split()
        marks.add(mark)

    return sorted(marks)


def test_append_item_to_list_multiple():
    lines =dedent("""\
    Harry 37.21
    Berry 37.21
    Tina 37.2
    Akriti 41
    Harsh 39
    """).splitlines()

    assert get_second_lowest(lines) == 5


if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        print(get_second_lowest(students))

