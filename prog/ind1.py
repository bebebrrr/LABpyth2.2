#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
if __name__=='__main__':
    c=int(input("value c? "))
    if c<0 or c>9:
        print("Error!", file=sys.stderr)
        exit(1)
    elif c==1:
        print("one")
    elif c==2:
        print("two")
    elif c==3:
        print("three")
    elif c==4:
        print("four")
    elif c==5:
        print("five")
    elif c==6:
        print("six")
    elif c==7:
        print("seven")
    elif c==8:
        print("eight")
    else:
        print("nine")
    