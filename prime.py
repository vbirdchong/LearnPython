#!/usr/bin/env python
# coding=utf-8

# serch the prime value in 2-100

import math

def isPrime(value):
    if value <= 1:
        return False
    for i in range(2, int(math.sqrt(value) + 1)):
        if value % i == 0:
            return False
    return True

for i in range(2,100):
    isFind = isPrime(i)
    if isFind:
        print i
