from .. import magic_index


def test_get_magic_index_if_input_is_distinct():
    sample_inputs_and_expected_answer = (
        ([-1, 0, 1, 3, 5, 6], 3),
        ([3, 4, 6, 7, 8], None),
        ([-1, 1, 3, 8, 10, 11], 1),
        ([], None),
    )
    for numbers, expected_answer in sample_inputs_and_expected_answer:
        answer = magic_index.get_magic_index_if_input_is_distinct(numbers)
        assert answer == expected_answer
