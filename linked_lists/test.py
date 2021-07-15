class A:
    pass


class B:
    pass


def do_something(some):
    some = B()


if __name__ == '__main__':
    a = A()
    print(a.__class__)
    do_something(a)
    print(a.__class__)
