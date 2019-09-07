"""
Problem

    A magic index in an array A[0...n-1] is defined to be an index such that
    A[i] = i. Given a sorted array of distinct integers, write a method to find
    a magic index, if one exists, in array A.

Follow up

    What if the values are not distinct?
"""

from typing import List, Optional


def get_magic_index_if_input_is_distinct(numbers: List[int]) -> Optional[int]:
    """Finds Magic index if exists

    Magic index is an index value in which index position is equal to value of
    element located in that sequence.

    This method expects that numbers in a given sequence are distinct and are
    always in increasing order.
    """
    start_index = 0
    end_index = len(numbers) - 1

    while start_index < end_index:
        middle_index = (start_index + end_index) // 2

        if middle_index == numbers[middle_index]:
            return middle_index
        elif middle_index > numbers[middle_index]:
            start_index = middle_index
        else:
            end_index = middle_index
    return None
