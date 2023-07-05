#!/usr/bin/python3
""" script that contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    li = list(set(list_of_integers))
    lo = len(li)
    if lo == 0:
        return
    m = lo // 2
    if (m == lo - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != lo - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
