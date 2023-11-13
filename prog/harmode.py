#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

eps=1e-10

if __name__=='__main__':
    n=int(input("n="))
    if n==0:
        print("Illegal value of n", file=sys.stderr)
        exit(1)
    x=int(input("x="))
    if x==0:
        print("Illegal value of x", file=sys.stderr)
        exit(1)
    a=x
    s, k=a, 1
    while math.fabs(a)<eps:
        a*=((-x**2/4)/(k+1)*(k+1+n))
        s+=a
        k+=1
    print(f"J {n}({x})={(x/2)**n*s}")
