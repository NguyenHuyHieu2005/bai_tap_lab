# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:18:03 2024

@author: ADM
"""

# Nhập ba số từ bàn phím
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
temp = 0

# So sánh và hoán đổi để sắp xếp theo thứ tự tăng dần
if a > b:
    temp = a
    a = b
    b = temp

if a > c:
    temp = a
    a = c
    c = temp

if b > c:
    temp = b
    b = c
    c = temp

# In kết quả theo thứ tự tăng dần
print("Thứ tự tăng dần là:", a, b, c)