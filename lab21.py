# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 17:14:30 2024

@author: ADM
"""

# Nhập số từ người dùng
so = int(input("Nhập 1 số nguyên: "))

# Kiểm tra số và in ra kết quả
if 0 <= so <= 9:
        chuoi_so = ["Không", "Một", "Hai", "Ba", "Bốn", "Năm", "Sáu", "Bảy", "Tám", "Chín"]
        print(chuoi_so[so])
else:
        print("Không đọc được")