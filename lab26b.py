# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:19:56 2024

@author: ADM
"""

N = int(input("nhập vào một số có 4 chữ số: "))  # Nhập số nguyên N

result = int("".join(sorted(str(N))))

print("kết quả là :", result)  # In ra số có các chữ số theo thứ tự tăng dần