"""
Problem

    How would you design a stack which, in addition to push and pop, has a
    function min which returns the minimum element? Push, pop, min should all
    operate in O(1) time.
"""
TOP_OF_THE_STACK = -1
MINIMUM = 1


class StackWithMin:

    def __init__(self):
        self._elements = []
        self._top_of_the_stack = None

    def push(self, number: int) -> None:
        if len(self._elements) == 0:
            self._elements.append(
                (number, number)
            )
        else:
            last_minimum_number = self._elements[TOP_OF_THE_STACK][MINIMUM]
            if number < last_minimum_number:
                minimum_number = number
            else:
                minimum_number = last_minimum_number
            self._elements.append((number, minimum_number))

    def pop(self) -> int:
        number, _ = self._elements.pop()
        return number

    def min(self) -> int:
        return self._elements[TOP_OF_THE_STACK][MINIMUM]
