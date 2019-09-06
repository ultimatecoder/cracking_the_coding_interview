"""
Problem

    You have two numbers represented by a linked list, where each node contains
    a single digit. The digits are stored in reverse order, such that the 1's
    digit is at the head of the list. Write a function that adds the two
    numbers and returns the sum as a linked list.

Example

    Input

        (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295

    Output

        2 -> 1 -> 9. That is, 912

Follow up

    Suppose the digits are stored in forward order. Repeat the above problem.

Example

    Input

        (6 -> 1 -> 7) + (2 + 9 + 5). That is, 617 + 295

    Output

        9 -> 1 -> 2. That is 912.
"""
from typing import Any


class Node:

    def __init__(self, value: Any):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self, elements=[]):
        self.head = None
        self._length = 0
        for element in elements[::-1]:
            self.add(element)

    def add(self, value: Any) -> None:
        self._length += 1
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def __eq__(self, another_list):
        if len(self) != len(another_list):
            return False
        pointer_to_first_list = self.head
        pointer_to_second_list = another_list.head
        while (
            (pointer_to_first_list is not None) and
            (pointer_to_second_list is not None) and
            (pointer_to_first_list.value == pointer_to_second_list.value)
        ):
            pointer_to_first_list = pointer_to_first_list.next
            pointer_to_second_list = pointer_to_second_list.next
        return pointer_to_first_list == pointer_to_second_list

    def __len__(self):
        return self._length


def sum_two_numbers(
    head_of_number_1: Node,
    head_of_number_2: Node,
    carry=0
) -> SinglyLinkedList:
    """Sums two numbers given as Singly Linked Lists.

    This method expects numbers to be constructed in reverse order.

    Let's observe how this method expects arguments when our purpose is to sum
    number "4328" with "925". So this method expects number "4328" as Singly
    linked list "8 -> 2 -> 3 -> 4" and number "925" as singly linked list "5 ->
    2 -> 9".

    Sum of these two numbers is "5253" which is returned by this method as a "3
    -> 5 -> 2 -> 5" instance of singly linked list.
    """
    if (
        (head_of_number_1 is None) and
        (head_of_number_2 is None)
    ):
        result_linked_list = SinglyLinkedList()
        if carry:
            result_linked_list.add(carry)
        return result_linked_list
    elif head_of_number_1 is None:
        _sum = head_of_number_2.value + carry
        head_of_number_2 = head_of_number_2.next
    elif head_of_number_2 is None:
        _sum = head_of_number_1.value + carry
        head_of_number_1 = head_of_number_1.next
    else:
        _sum = head_of_number_1.value + head_of_number_2.value + carry
        head_of_number_1 = head_of_number_1.next  # type: ignore
        head_of_number_2 = head_of_number_2.next  # type: ignore

    if _sum > 9:
        _sum = _sum % 10
        carry = 1
    else:
        carry = 0
    result_linked_list = sum_two_numbers(
        head_of_number_1,
        head_of_number_2,
        carry=carry
    )
    result_linked_list.add(_sum)
    return result_linked_list
