#!/usr/bin/env python
# coding=utf-8

# quadratic equation



def quadratic_equation(a, b, c):
    dalta = b*b - 4*a*c
    if dalta < 0:
        return False
    elif dalta == 0:
        return -(b/(2*c))
    else:
        sqrt_delta = math.sqrt(dalta)
        x1 = (-b + sqrt_delta)/(2*a)
        x2 = (-b - sqrt_delta)/(2*a)
        return x1, x2


ret = quadratic_equation(1,2,1)
if ret:
    print "This equation have roots:", ret
else:
    print "This equation have no roots"
