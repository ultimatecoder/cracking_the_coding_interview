#! /usr/bin/env python
"""
Problem

    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

Notes:

    Below are few unanswered questions in this problem.

        1. Should small case and upper case characters will be part of string?

            I have considered them equal. Means, character 'A' and 'a' are
            same.

        2. Will special characters like '*', '/', '%' be a part of string?

            These solutions will assume that they will be part of a string.

        3. Will there be any white-space in a string? If yes, then should two
           white-spaces be considered as same?

            Below solutions are not considering a white space as same. All
            white-spaces in a string are ignored.

        4. Can a string be empty?

            These solutions are developed by assuming that a given string can
            be empty.

        5. Are characters ASCII?

            Below solutions are developed by assuming that there will be only
            ASCII characters in string.

"""
from typing import Set, Union


def brute_force(characters: str) -> bool:
    """Identifies that characters in given string are unique

    This method is an implementation of the brute force approach. This method
    do not use any external data structures.

    * Complexity:

        * Time: O(N^2)
        * Space: O(1)
    """
    for first_pointer in range(len(characters)):
        for second_pointer in range(first_pointer + 1, len(characters)):
            first_character = characters[first_pointer].upper()
            second_character = characters[second_pointer].upper()

            if first_character == ' ':
                break
            elif second_character == ' ':
                continue
            elif first_character == second_character:
                return False
    return True


def bit_array(characters: str) -> bool:
    """Identifies that characters in given string are unique

    This method is based on Bit Array [1]. It pre-defines an iterable of
    boolean type having 0 as a default value. Length of it is combined length
    of all 26 alphabets, 9 digits and 32 special characters.  Each character
    will be resolved to a unique index in first and then registered its
    presence by shifting its bit value.

    Presence of any character is registered by following below Algorithm:

        * Find index of given character.
        * If value for that index in an bit array is 0 (zero), then convert it
          to one.
        * If value for that index in an bit array is not 0 (zero), then
          consider that this character has identified before.

    Complexity:

        * Time: O(N)
        * Space: O(68)

    1: https://en.wikipedia.org/wiki/Bit_array
    """
    register = [0 for _ in range(68)]
    for character in characters:

        if character == ' ':
            continue
        else:
            character = character.lower()
            index = _get_index(character)
            if index is None:
                raise ValueError(
                    f"Given character {character} is not supported"
                )
            if register[index] == 1:
                return False
            else:
                register[index] = 1
    return True


def hash_table(characters: str) -> bool:
    """Identifies duplicate characters using Hash-table approach

    This method follows below Algorithm to identify duplicate characters in
    given String.

        * If given character is present in Hash-table, terminate
        * If given character is not present in Hash-table, add it to a
          hash-table and move to next character.

    Complexity:

        * Time: O(N)
        * Space: O(N)
    """
    register: Set[str] = set()
    for character in characters:
        if character == ' ':
            continue
        else:
            character = character.lower()
        if character in register:
            return False
        else:
            register.add(character)
    return True


def _get_index(character: str) -> Union[int, None]:
    """ Returns index of given character

    Below are range of indexes mainly distributed in three parts.
        1. Alphabets (abcdefghijklmnopqrstuvwxyz)
        2. Digits (01234567)
        3. Special symbols ('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

    Index ranges:
        * 0 to 14
            Special characters !"#$%&\'()*+,-.

        * 15 to 24
            Digits 01234567

        * 25 to 31
            Special characters :;<=>?@

        * 32 to 37
            Special characters [\\]^_`

        * 38 to 63
            Alphabets abcdefghijklmnopqrstuvwxyz

        * 64 to 67
            Special character symbols |}~
    """
    ascii_index = ord(character)

    if (
        ((ascii_index >= 33) and (ascii_index <= 47)) or
        ((ascii_index >= 48) and (ascii_index <= 57)) or
        ((ascii_index >= 58) and (ascii_index <= 64))
    ):
        return ascii_index - 33
    elif (
        ((ascii_index >= 91) and (ascii_index <= 96)) or
        ((ascii_index >= 97) and (ascii_index <= 122)) or
        ((ascii_index >= 123) and (ascii_index <= 126))
    ):
        return ascii_index - 59
    else:
        return None
