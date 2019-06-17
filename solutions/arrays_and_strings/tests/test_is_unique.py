#! /usr/bin/env python

from .. import is_unique

sample_strings_and_expected_answers = (
    ("", True),
    ("a b c", True),
    ("aba", False),
    ("abA", False),
    ("AbCDefgh", True),
    ("Hello World", False),
    ("He is not Ramu", True),
    ('He said, "#%^@@ you!"', False),
    ("F$%@ you!", True)
)


def test_is_unique_brute_force():
    for sample_string, expected_answer in sample_strings_and_expected_answers:
        assert is_unique.brute_force(sample_string) == expected_answer


def test_is_unique_bit_array():
    for sample_string, expected_answer in sample_strings_and_expected_answers:
        assert is_unique.bit_array(sample_string) == expected_answer


def test_is_unique_hash_table():
    for sample_string, expected_answer in sample_strings_and_expected_answers:
        assert is_unique.hash_table(sample_string) == expected_answer
