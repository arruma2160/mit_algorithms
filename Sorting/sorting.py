#! /usr/bin/env python3
from functools import wraps
from timeit import default_timer as timer


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = timer()
        res = func(*args, **kwargs)
        elapsed = timer() - t1
        print(f"{func.__name__: <16} -> {elapsed: <10} seconds")
        return res
    return wrapper


@execution_time
def insertion_sort(l):
    for j in range(1, len(l)):
        key = l[j]
        i = j-1
        while i>=0 and l[i]>key:
            l[i+1] = l[i]
            i -= 1
        l[i+1] = key
    return l


@execution_time
def brute_sort(l):
    for i in range(0, len(l)):
        min, m = l[i], i
        for k in range(i+1, len(l)):
            if l[k] < min:
                min, m = l[k], k
        l[i], l[m] = l[m], l[i]
    return l


@execution_time
def bubble_sort(l):
    for i in range(0, len(l)-1):
        for j in range(0, len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


@execution_time
def merge_sort(l):
    def merge(l, p, q, r):
        sol = list()
        i = p
        k = q+1
        z = p
        while (i!=q+1) and (k!=r+1):
            if l[i] < l[k]:
                sol.append(l[i])
                i += 1
            else: # l[i] >= l[k]
                sol.append(l[k])
                k += 1
            z += 1

        if i == q+1:
            sol += l[k:r+1]
        else:
            sol += l[i:q+1]

        l[p:r+1] = sol[:]

    def _merge_sort(l, p, r):
        if p < r:
            q = (p+r)//2
            _merge_sort(l, p, q)
            _merge_sort(l, q+1, r)
            merge(l, p, q, r)
        return l

    return _merge_sort(l, 0, len(l)-1)


def exercise_sorting_algorithms_and_display_performance():
    '''Long array test (random) - assess correctness and get feedback on the
    execution time employed by the algorithm
    '''
    import numpy as np
    random_element_list = np.random.randint(10**10, size=10**5).tolist()

    test = random_element_list[:]
    result = insertion_sort(test)
    for i in range(1,len(test)):
        # Assert correctness
        assert result[i-1] <= result[i]

    test = random_element_list[:]
    result = brute_sort(test)
    for i in range(1,len(test)):
        # Assert correctness
        assert result[i-1] <= result[i]

    test = random_element_list[:]
    result = bubble_sort(test)
    for i in range(1,len(test)):
        # Assert correctness
        assert result[i-1] <= result[i]

    test = random_element_list[:]
    result = merge_sort(test)
    for i in range(1,len(test)):
        # Assert correctness
        assert result[i-1] <= result[i]


if __name__ == "__main__":
    exercise_sorting_algorithms_and_display_performance()
