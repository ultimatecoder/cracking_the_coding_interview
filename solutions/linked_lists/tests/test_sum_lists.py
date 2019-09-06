from .. import sum_lists


def test_node():
    node = sum_lists.Node(2)
    assert node.value == 2
    assert node.next is None


def test_singly_linked_list_is_able_to_initialize():
    sample_numbers = (
        [1, 1, 2, 3],
        [],
        [-1, 0],
        [0],
    )
    for numbers in sample_numbers:
        _list = sum_lists.SinglyLinkedList(numbers)
        head = _list.head
        for number in numbers:
            assert head.value == number
            head = head.next


def test_singly_linked_list_add():
    _list = sum_lists.SinglyLinkedList()
    numbers = [1, 3, 4, 5, 5, 6]
    for number in numbers:
        _list.add(number)
    head = _list.head
    numbers.reverse()
    for number in numbers:
        assert head.value == number
        head = head.next


def test_singly_linked_list_length():
    sample_inputs = (
        [1, 2, 3],
        [1, 1],
        [],
        [1, -1, 1, -1, 0]
    )
    for sample_input in sample_inputs:
        _list = sum_lists.SinglyLinkedList(sample_input)
        assert len(_list) == len(sample_input)


def test_singly_linked_list_equal():
    sample_inputs_and_expected_answer = (
        (
            sum_lists.SinglyLinkedList([1, 1, 1]),
            sum_lists.SinglyLinkedList([1, 1, 1]),
            True
        ),
        (
            sum_lists.SinglyLinkedList([]),
            sum_lists.SinglyLinkedList([]),
            True
        ),
        (
            sum_lists.SinglyLinkedList([-1, 0, 1, 2]),
            sum_lists.SinglyLinkedList([1, 2, 0, -1]),
            False
        ),
        (
            sum_lists.SinglyLinkedList([-1]),
            sum_lists.SinglyLinkedList([]),
            False
        ),
        (
            sum_lists.SinglyLinkedList([-1, 2]),
            sum_lists.SinglyLinkedList([1, 2, 0, -1]),
            False
        ),
        (
            sum_lists.SinglyLinkedList([-1, 2, 1]),
            sum_lists.SinglyLinkedList([-1, 2, 0]),
            False
        ),
    )
    for list_1, list_2, expected_answer in (
        sample_inputs_and_expected_answer
    ):
        answer = (list_1 == list_2)
        assert answer == expected_answer


def test_sum_list_backward():
    sample_numbers_and_expected_answers = (
        ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        ([], [], []),
        ([], [1, 3], [1, 3]),
        ([0, 1, 4], [], [0, 1, 4]),
        ([9, 9, 9, 9], [9, 9, 9], [8, 9, 9, 0, 1]),
        ([4, 1, 3, 8], [8, 9, 9], [2, 1, 3, 9]),
    )

    for numbers_1, numbers_2, expected_numbers in (
        sample_numbers_and_expected_answers
    ):
        list_1 = sum_lists.SinglyLinkedList(numbers_1)
        list_2 = sum_lists.SinglyLinkedList(numbers_2)
        expected_list = sum_lists.SinglyLinkedList(expected_numbers)
        result_list = sum_lists.sum_two_numbers(list_1.head, list_2.head)
        assert result_list == expected_list
