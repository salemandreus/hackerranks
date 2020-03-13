from collections import namedtuple
from textwrap import dedent

Student = namedtuple('Student', 'ID, MARKS, NAME, CLASS' )


def parse_input(lines):

    Student = namedtuple('Student', lines[0])

    student1 = Student(lines[1])

    return student1


def get_average(*args):
    pass


# def test_parse_empty():
#     lines = "i,t".splitlines()
#
#     assert parse_input(lines) == 'Student("ID=1, MARKS=97, NAME=Raymond, CLASS=7")'


# def test_parse_empty():
#     lines = dedent("""\
#         ID, MARKS, NAME, CLASS
#         , , ,
#     """).splitlines()
#
#     assert parse_input(lines) == 'Student("ID=1, MARKS=97, NAME=Raymond, CLASS=7")'


def test_parse_one_line():
    lines = dedent("""\
        ID, MARKS, NAME, CLASS
        1, 97, Raymond, 7
    """).splitlines()

    assert parse_input(lines) == 'Student("ID=1, MARKS=97, NAME=Raymond, CLASS=7")'


def test_parse():
    lines = dedent("""\
        ID, MARKS, NAME, CLASS
        1, 97, Raymond, 7
        2, 50, Steven, 4
        3, 91, Adrian, 9
        4, 72, Stewart, 5
        5, 80, Peter, 6
""").splitlines()

    # dedent("""\
    #     Lions 3, Snakes 3	    Lions 3, Snakes 3
    #     Tarantulas 1, FC Awesome 0	    Tarantulas 1, FC Awesome 0
    #     Lions 1, FC Awesome 1	    Lions 1, FC Awesome 1
    #     Tarantulas 3, Snakes 1	    Tarantulas 3, Snakes 1
    #     Lions 4, Grouches 0	    Lions 4, Grouches 0
    # """)
    # """).splitlines()

    assert parse_input(lines) == False

def test_average():
    """
    5
    ID         MARKS      NAME       CLASS
    1          97         Raymond    7
    2          50         Steven     4
    3          91         Adrian     9
    4          72         Stewart    5
    5          80         Peter      6
    """



    assert get_average("a","b","c") == ("a","b","c")


