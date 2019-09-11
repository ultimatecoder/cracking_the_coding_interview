from typing import Tuple

from .. import group_anagrams


def test_brute_force_sort():
    sample_inputs_and_expected_outputs: Tuple = (
        (
            ["aa", "bb", "acca", "bb", "aa", "ccaa"],
            ['aa', 'aa', 'acca', 'ccaa', 'bb', 'bb']
        ),
        ([], []),
        (
            ["a", "b", "c", "a", "b", "c"],
            ["a", "a", "c", "c", "b", "b"]
        )
    )

    brute_force = group_anagrams.BruteForce()
    for anagrams, expected_anagrams in sample_inputs_and_expected_outputs:
        brute_force.sort(anagrams)
        assert anagrams == expected_anagrams


def test_improved_sort():
    sample_inputs_and_expected_outputs: Tuple = (
        (
            ["aa", "bb", "acca", "bb", "aa", "ccaa"],
            ['ccaa', 'acca', 'aa', 'aa', 'bb', 'bb']
        ),
        ([], []),
        (
            ["a", "b", "c", "a", "b", "c"],
            ['c', 'c', 'b', 'b', 'a', 'a']
        )
    )
    improved = group_anagrams.Improved()
    for anagrams, expected_anagrams in sample_inputs_and_expected_outputs:
        improved.sort(anagrams)
        assert anagrams == expected_anagrams
