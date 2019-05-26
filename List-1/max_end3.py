"""
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""

def max_end3(nums):
    new = []
    first = nums[0]
    last = nums[len(nums)-1]
    if first > last:
        for i in range(len(nums)):
            new.append(first)
    elif first < last:
        for i in range(len(nums)):
            new.append(last)
    else:
        for i in range(len(nums)):
            new.append(last)
    return new