def execute_commands(commands):
    ls = []
    for command in commands:
        parts = command.split()
        if parts[0] == "print":
            yield str(ls)
        elif parts[0] == "insert":
            ls.insert(int(parts[1]), int(parts[2]))
        elif parts[0] == "remove":
            ls.remove(int(parts[1]))
        elif parts[0] == "append":
            ls.append(int(parts[1]))
        elif parts[0] == "sort":
            ls.sort()
        elif parts[0] == "pop":
            ls.pop()
        elif parts[0] == "reverse":
            ls.reverse()
        else:
            # print (parts[0])
            yield "unimplemented: ", parts


def test_command_reader():
    assert list(execute_commands([])) == []
    assert list(execute_commands(['print'])) == ['[]']

    assert list(execute_commands([
        'insert 0 5',
        'insert 1 10',
        'insert 0 6',
        'print',
        'remove 6',
        'append 9',
        'append 1',
        'sort',
        'print',
        'pop',
        'reverse',
        'print',
    ])) == [
        '[6, 5, 10]',
        '[1, 5, 9, 10]',
        '[9, 5, 1]',
    ]


if __name__ == '__main__':
    N = int(input())
    commands = [input() for _ in range(N)]
    for output in execute_commands(commands):
        print(output)

