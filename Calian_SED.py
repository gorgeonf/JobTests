#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:35:51 2020

@author: florian
"""

'''
Write functions that calculate the nth Fibonacci number
in O(n) time or better without using any "for" or "while" loops.
'''

n = input("Enter an integer: ")
cache = {}


# Write functions that calculate the nth Fibonacci number
# in O(n) time or better without using any "for" or "while" loops.
def Fibonacci(n):
    global cpt
    if n in cache:
        return cache[n]
    if (n == 1 or n == 2):
        res = 1
    else:
        res = Fibonacci(n - 1) + Fibonacci(n - 2)
        cpt += 1
    cache[n] = res
    return res


cpt = 0
print(str(n) + "th term of the series: " + str(Fibonacci(int(n))) + " in O(" + str(cpt) + ")")
