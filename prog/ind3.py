#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from prettytable import PrettyTable

if __name__=='__main__':
 
 a=int(input("a= "))
 myTable= PrettyTable(["funts", "kg"])
 #print("| Вес в фунтах | Вес в килограммах |")
 for i in range (1, a, 1):
  f=i*400
  l=f/1000
  myTable.add_row(["{0}", "{1}".format(i,l)])
  #print("| {0} | {1} |".format(i, l))