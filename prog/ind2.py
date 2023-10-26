#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__=='__main__':
    a=float(input("a= "))
    b=float(input("b= "))
    c=float(input("c= "))
    d=b**2+4*a*c
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-)/2*a
    print("x1={x1}, x2={x2}")