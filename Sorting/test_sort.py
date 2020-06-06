#! /usr/bin/env python3
import pytest

from sorting import insertion_sort, brute_sort, bubble_sort, merge_sort


def test_insertion_sort():
    l = [66, 76,  3, 38, 25, 20, 97,  8,  1,  2, 58, 20, 69, 81, 57, 23, 32,
         42, 85, 74, 43, 51, 51,  3, 49, 50, 27, 37, 40, 92]

    expectation = [1, 2, 3, 3, 8, 20, 20, 23, 25, 27, 32, 37, 38, 40, 42, 43,
            49, 50, 51, 51, 57, 58, 66, 69, 74, 76, 81, 85, 92, 97]

    result = insertion_sort(l)
    assert result == expectation, f"{result}"


def test_brute_sort():

    l = [66, 76,  3, 38, 25, 20, 97, 8,  1,  2, 58, 20, 69, 81, 57, 23, 32,
         42, 85, 74, 43, 51, 51, 3, 49, 50, 27, 37, 40, 92]

    expectation = [1, 2, 3, 3, 8, 20, 20, 23, 25, 27, 32, 37, 38, 40, 42, 43,
            49, 50, 51, 51, 57, 58, 66, 69, 74, 76, 81, 85, 92, 97]

    result = brute_sort(l)
    assert result == expectation, f"{result}"


def test_bubble_sort():

    l = [66, 76,  3, 38, 25, 20, 97, 8,  1,  2, 58, 20, 69, 81, 57, 23, 32,
         42, 85, 74, 43, 51, 51, 3, 49, 50, 27, 37, 40, 92]

    expectation = [1, 2, 3, 3, 8, 20, 20, 23, 25, 27, 32, 37, 38, 40, 42, 43,
            49, 50, 51, 51, 57, 58, 66, 69, 74, 76, 81, 85, 92, 97]

    result = bubble_sort(l)
    assert result == expectation, f"{result}"


def test_merge_sort():

    l = [66, 76,  3, 38, 25, 20, 97, 8,  1,  2, 58, 20, 69, 81, 57, 23, 32,
         42, 85, 74, 43, 51, 51, 3, 49, 50, 27, 37, 40, 92]

    expectation = [1, 2, 3, 3, 8, 20, 20, 23, 25, 27, 32, 37, 38, 40, 42, 43,
            49, 50, 51, 51, 57, 58, 66, 69, 74, 76, 81, 85, 92, 97]

    result = merge_sort(l)
    assert result == expectation, f"{result}"
