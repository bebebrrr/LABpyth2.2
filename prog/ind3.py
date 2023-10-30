#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__=='__main__':
 
 a=int(input("a= "))
 print("--------------")
 print("| funts | kg  |")
 print("--------------")
 for i in range (1, a, 1):
  f=i*400
  l=f/1000
  print("| {0}     | {1} |".format(i, l))
  print("--------------")