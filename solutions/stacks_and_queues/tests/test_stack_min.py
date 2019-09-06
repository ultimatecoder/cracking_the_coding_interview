from .. import stack_min


def test_stack_push():
    numbers = [
        (1, 1),
        (2, 1),
        (1, 1),
        (0, 0),
        (0, 0),
        (4, 0),
        (5, 0)
    ]
    stack = stack_min.StackWithMin()
    for number, expected_number in numbers:
        stack.push(number)
        assert stack.min() == expected_number


def test_stack_pop():
    numbers = [
        (4, 4),
        (5, 4),
        (2, 2),
        (-1, -1),
        (2, -1)
    ]
    stack = stack_min.StackWithMin()
    for number, _ in numbers:
        stack.push(number)

    for expected_number, expected_minimum_number in numbers[::-1]:
        assert stack.min() == expected_minimum_number
        number = stack.pop()
        assert number == expected_number
