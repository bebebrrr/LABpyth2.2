#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__=='__main__':
    a=float(input("a= "))
    while a==0:
    
        print("а должно быть больше 0!")
        a=float(input("a= "))
    b=float(input("b= "))
    c=float(input("c= "))
    d=b**2+4*a*c
    x1=(-b+ math.sqrt(d))/2*a
    x2=(-b- math.sqrt(d))/2*a
    print(f"x1={x1}, x2={x2}")