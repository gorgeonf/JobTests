#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 16:48:06 2020

@author: florian
"""


def fizzbuzz(n):
    for i in range(0, n, 1):
        i += 1
        if i % 3 == 0: print("Fizz", end='')
        if i % 5 == 0: print("Buzz", end='')
        if (i % 3 != 0) & (i % 5 != 0): print(i, end='')
        print()


fizzbuzz(15)
