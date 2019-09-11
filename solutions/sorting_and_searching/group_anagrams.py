"""
Problem

    Write a method to sort an array of strings so that all the anagrams are
    next to each other.
"""
from collections import defaultdict
from typing import List, Dict


class BruteForce:
    """Brute force implementation of group anagrams"""

    def _is_anagrams(self, string_1: str, string_2: str) -> bool:
        if len(string_1) != len(string_2):
            return False
        character_count: Dict = defaultdict(int)
        for character in string_1:
            character_count[character] += 1
        for character in string_2:
            if (
                (character not in character_count) or
                (character_count[character] == 0)
            ):
                return False
            else:
                character_count[character] -= 1
        return True

    def sort(self, anagrams: List[str]) -> None:
        if not anagrams:
            return None
        index = 0
        while index < len(anagrams):
            for index_of_left in range(index + 1, len(anagrams)):
                if self._is_anagrams(
                    anagrams[index], anagrams[index_of_left]
                ):
                    anagrams[index + 1], anagrams[index_of_left] = (
                        anagrams[index_of_left], anagrams[index + 1]
                    )
                    break
            index += 2
        return


class Improved:
    """Improved implementation to group anagrams"""

    def _calculate_score(self, anagram: str) -> int:
        score = 0
        for character in anagram:
            score += ord(character)
        return score

    def sort(self, anagrams):
        anagrams_collection = defaultdict(list)
        while len(anagrams) != 0:
            anagram = anagrams.pop()
            score = self._calculate_score(anagram)
            anagrams_collection[score].append(anagram)
        for _, similar_anagrams in anagrams_collection.items():
            for anagram in similar_anagrams:
                anagrams.append(anagram)
