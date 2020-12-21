#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Write functions that calculate the nth Fibonacci number
in O(n) time or better without using any "for" or "while" loops.
"""

n = input("Enter an integer: ")
cache = {}


# Write functions that calculate the nth Fibonacci number
# in O(n) time or better without using any "for" or "while" loops.
def fibonacci(i):
    global cpt
    if i in cache:
        return cache[i]
    if i == 1 or i == 2:
        res = 1
    else:
        res = fibonacci(i - 1) + fibonacci(i - 2)
        cpt += 1
    cache[i] = res
    return res


cpt = 0
print(str(n) + "th term of the series: " + str(fibonacci(int(n))) + " in O(" + str(cpt) + ")")
