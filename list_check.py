#!/usr/bin/env python

def list_check(vals):
    # all will return True only when all the elements are Truthy
    return all(type(l) == list for l in vals)


print(list_check([[], [1], [2, 3], (1, 2)]))  # False
list_check([1, True, [], [1], [2, 3]])  # False
list_check( [ [], [1], [2, 3] ] )  # True
