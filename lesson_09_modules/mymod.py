def count_lines(name):
    with open(name, "r") as f:
        return len(f.readlines())


def count_chars(name):
    with open(name, "r") as f:
        return len(f.read())

def test(name):
    print(count_lines(name))
    print(count_chars(name))

def count_lines2(f):
    return len(f.readlines())


def count_chars2(f):
    return len(f.read())

def test2(name="task-1.py"):
    with open(name, "r") as f:
        print(count_lines2(f))
        f.seek(0)
        print(count_chars2(f))