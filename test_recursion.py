from collections import Counter

import pytest
from RecursionAndBacktracking import permutation, isPermutation, minMoves


@pytest.mark.parametrize("text, expected", [
    ("", [""]),
    ("a", ["a"]),
    ("ab", ["ab", "ba"]),
    ("abc", ["abc", "acb", "bac", "bca", "cab", "cba"]),
    # The current implementation permutes indices, so duplicates are preserved.
    ("aa", ["aa", "aa"]),
    ("aab", ["aab", "aba", "aab", "aba", "baa", "baa"]),
])
def test_permutation(text, expected):
    assert Counter(permutation(text)) == Counter(expected)


@pytest.mark.parametrize("s1, s2, expected", [
    ("ab", "eidbaooo", True),
    ("ab", "eidboaoo", False),
    ("abc", "bca", True),
    ("abc", "xxcab", True),
    ("abc", "abcxx", True),
    ("abc", "axbyc", False),
    ("abcd", "abc", False),
    ("aab", "xxaba", True),
    ("aab", "abb", False),
    ("aaa", "baaa", True),
    ("aaa", "aaba", False),
    ("a", "cat", True),
    ("z", "cat", False),
    ("ab", "", False),
    # Python treats the empty string as a substring of every string.
    ("", "abc", True),
    ("", "", True),
])
def test_is_permutation(s1, s2, expected):
    assert isPermutation(s1, s2) is expected


@pytest.mark.parametrize("queens, expected", [
    ([1, 2, 3, 4, 5, 6, 7, 8], 7),
    ([1, 1, 1, 1, 1, 1, 1, 1], 7),
    ([8, 8, 8, 8, 8, 8, 8, 8], 7),
    ([8, 7, 6, 5, 4, 3, 2, 1], 7),
    ([1, 5, 8, 6, 3, 7, 2, 4], 0),
    ([4, 2, 7, 3, 6, 8, 5, 1], 0),
    ([1, 5, 8, 6, 3, 7, 2, 1], 1),
    ([4, 5, 8, 6, 3, 7, 2, 4], 1),
    ([1, 5, 8, 6, 3, 7, 1, 1], 2),
])
def test_min_moves(queens, expected):
    assert minMoves(queens) == expected


def test_min_moves_keeps_input_unchanged():
    queens = [1, 5, 8, 6, 3, 7, 1, 1]
    original = queens.copy()
    minMoves(queens)
    assert queens == original


def test_min_moves_repeated_calls():
    assert minMoves([1, 1, 1, 1, 1, 1, 1, 1]) == 7
    assert minMoves([1, 5, 8, 6, 3, 7, 2, 4]) == 0
    assert minMoves([1, 1, 1, 1, 1, 1, 1, 1]) == 7
