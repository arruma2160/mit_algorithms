#! /usr/bin/env python3

def unidimensional_peak_finder(l):
    '''Accepts a list of integer values and returns the/a peak value.'''
    assert isinstance(l, list)

    i = len(l)//2

    if len(l) <= 2:
        if len(l) == 1:
            return 0
        if len(l) == 2:
            return 0 if l[0]>=l[1] else 1
    elif l[i] > l[i-1]:
        return i + unidimensional_peak_finder(l[i:])
    elif l[i] > l[i+1]:
        return unidimensional_peak_finder(l[0:i+1])
    else:
        return i


def bidimensional_peak_finder(l):
    '''Accepts a list of lists of integer values and returns the position of
    the/a peak value.'''
    print(l)

    i = len(l)//2
    j = unidimensional_peak_finder(l[i])

    if len(l) <= 2:
        if len(l) == 1:
            return (0, j)
        elif len(l) == 2:
            if l[0][j] > l[1][j]:
                return (0, j)
            else:
                return (1, j)
    elif l[i][j] > l[i-1][j]:
        (ir, jr) = bidimensional_peak_finder(l[i:])
        return (i+ir,jr)
    elif l[i][j] > l[i+1][j]:
        return bidimensional_peak_finder(l[:i])

    return (i, j)
