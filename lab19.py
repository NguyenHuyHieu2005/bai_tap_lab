# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:43:31 2024

@author: ADM
"""

# Nhập vào 4 số nguyên
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
d = int(input("Nhập số d: "))
minn = a

if b < minn:
    minn = b
if c < minn:
    minn = c

if d < minn:
    minn = d
print("Số nhỏ nhất là:", minn)