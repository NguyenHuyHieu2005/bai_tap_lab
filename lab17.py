# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 23:57:56 2024

@author: ADM
"""

# Nhập ba số nguyên
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

# Tìm số lớn nhất và nhỏ nhất
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)

# In kết quả
print("Số lớn nhất là: ", so_lon_nhat)
print("Số nhỏ nhất là: ", so_nho_nhat)
