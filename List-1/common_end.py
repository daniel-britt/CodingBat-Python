"""
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""

def common_end(a, b):
    firsta = a[0]
    firstb = b[0]
    lasta = a[len(a)-1]
    lastb = b[len(b)-1]
    if firsta == firstb or lasta == lastb:
        return True
    else:
        return False