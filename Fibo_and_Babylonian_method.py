#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 08:09:13 2020

@author: florian
"""

"""
        CODE IN C
/**
 * FIBONACCI SEQUENCE
 * F(n) = F(n-1) + F(n-2)
 * 		with F(0) = F(1) = 1
 * 	F(5) =                     F(4)            +             F(3)
 * 	F(5) =         F(3)         +      F(2)    +      F(2)     +   F(1)
 * 	F(5) =     F(2) + F(1)      +  F(1) + F(0) +   F(1) + F(0) +   F(1)
 * 	F(5) = F(1) + F(0)  +  F(1) +  F(1) + F(0) +   F(1) + F(0) +   F(1)
 *   F(5) =  1   +  1    +   1   +   1   +  1    +   1   +  1   +    1
 *   F(5) =  8
 *
 *   F = 1, 1, 2, 3, 5, 8, 13, 21...
 **/

//	Write functions that calculate the nth Fibonacci number
//	in O(n) time or better without using any "for" or "while" loops.
int Fibo(int n, int &cpt) {
	cpt++;
	if (n < 3) {
		return 1;
	} else {
		return Fibo(n - 1, cpt) + Fibo(n - 2, cpt);
	}
}

int Fibo(int n, int *const cpt) {
	// Increment the value pointed by cpt
	// /!\ Operators precedence : "++" over "*"
	(*cpt)++;
	if (n < 3) {
		return 1;
	} else {
		return Fibo(n - 1, cpt) + Fibo(n - 2, cpt);
	}
}

/**
 * THE BABYLONIAN METHOD (AKA, HERO'S METHOD) FOR FINDING SUARE ROOTS
 */
// RECURSIVE
double SqrtStep(double x, int step) {
	if (step == 0) {
		return x / 2;
	} else {
		step--;
		double xPrev = SqrtStep(x, step);
		return (x / xPrev + xPrev) / 2;
	}
}
// NON RECURSIVE
double BabyloninanSqrt(double x) {
	double epsilon = 1E-10;
	// Guess
	double xPrev = x / 2;
	double xCur = x;
	while (abs(xCur - xPrev) > epsilon) {
		xPrev = xCur;
		xCur = (x / xPrev + xPrev) / 2;
	}
	return xCur;
}
"""

n = 17


def fibo_1(i):
    global cpt
    if i == 1 or i == 2:
        res = 1
    else:
        res = fibo_1(i - 1) + fibo_1(i - 2)
    cpt += 1
    return res


# Write functions that calculate the nth Fibonacci number
# in O(n) time or better without using any "for" or "while" loops.
def fibonacci(i):
    if 'cache' not in locals():
        cache = {}
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
print(str(n) + "th term of the series: " + str(fibo_1(n)) + " in O(" + str(cpt) + ")")
cpt = 0
print(str(n) + "th term of the series: " + str(fibonacci(n)) + " in O(" + str(cpt) + ")")
