#! /usr/bin/env python3
import pytest

from peak_finder import unidimensional_peak_finder, \
                        bidimensional_peak_finder


def test_unidimensional_peak_finder_second_half():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 2, 0]
    res = unidimensional_peak_finder(l)
    assert res == 7, \
            f"Found on position: {res}, while 'input': {l}"


def test_unidimensional_peak_finder_first_half():
    l = [0, 1, 7, 4, 3, 2, 0]
    res = unidimensional_peak_finder(l)
    assert res == 2, \
            f"Found on position: {res}, while 'input': {l}"


def test_unidimensional_peak_finder_last_element():
    l = [13, 14, 15, 16, 17, 18]
    res = unidimensional_peak_finder(l)
    assert res == 5, \
            f"Found on position: {res}, while 'input': {l}"


def test_unidimensional_peak_finder_first_element():
    l = [24, 23, 22, 21, 20,  7]
    res = unidimensional_peak_finder(l)
    assert res == 0, \
            f"Found on position: {res}, while 'input': {l}"


def test_unidimensional_peak_finder_one_element_list():
    l = [1]
    res = unidimensional_peak_finder(l)
    assert res == 0, \
            f"Found on position: {res}, while 'input': {l}"


def test_unidimensional_peak_finder_two_element_list():
    l = [1, 2]
    res = unidimensional_peak_finder(l)
    assert res == 1, \
            f"Found on position: {res}, while 'input': {l}"


def test_unidimensional_peak_finder_three_element_list():
    l = [1, 3, 2]
    res = unidimensional_peak_finder(l)
    assert res == 1, \
            f"Found on position: {res}, while 'input': {l}"


def test_bidimensional_peak_finder_count_up_sequential():
    l = [[ 1,  2,  3,  4,  5,  6],
         [ 7,  8,  9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18],
         [19, 20, 21, 22, 23, 24]]

    res = bidimensional_peak_finder(l)
    assert res == (3, 5)


def test_bidimensional_peak_finder_count_up_sequentially_random_4_4():
    l = [[ 1,  2,  3,  4,  5,  6],
         [24, 23, 22, 21, 20,  7],
         [15, 16, 17, 18, 19,  8],
         [14, 13, 12, 11, 10,  9]]

    res = bidimensional_peak_finder(l)
    assert res == (1, 0)


def test_bidimensional_peak_finder_count_up_notes_example():
    l = [[10,  8, 10, 10],
         [14, 13, 12, 11],
         [15,  9, 11, 21],
         [16, 17, 19, 20]]

    res = bidimensional_peak_finder(l)
    assert res == (2, 3)
