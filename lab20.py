# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:48:28 2024

@author: ADM
"""

# Nhập vào 4 số nguyên
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
maxx = a

if b > maxx:
    maxx = b
if c > maxx:
    maxx = c

print("Số nhỏ nhất là:", maxx)