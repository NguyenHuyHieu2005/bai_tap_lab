# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:21:52 2024

@author: ADM
"""

import math

# Nhập loại hình
hinh = input("Nhập hình (v: hình vuông, n: hình chữ nhật, t: hình tròn): ")

if hinh == 'v':
    # Tính diện tích và chu vi của hình vuông
    canh = float(input("Nhập độ dài cạnh của hình vuông: "))
    chuvi = 4 * canh
    dientich = canh * canh
    print(f"P = {chuvi} S = {dientich}")

elif hinh == 'n':
    # Tính diện tích và chu vi của hình chữ nhật
    chieurong = float(input("Nhập chiều rộng của hình chữ nhật: "))
    chieudai = float(input("Nhập chiều dài của hình chữ nhật: "))
    chuvi = 2 * (chieurong + chieudai)
    dientich = chieurong * chieudai
    print(f"P = {chuvi} S = {dientich}")

elif hinh == 't':
    # Tính diện tích và chu vi của hình tròn
    bankinh = float(input("Nhập bán kính của hình tròn: "))
    chuvi = 2 * math.pi * bankinh
    dientich = math.pi * bankinh * bankinh
    print(f"P = {chuvi:.2f} S = {dientich:.2f}")

else:
    print("Loại hình không hợp lệ. Vui lòng nhập v, n hoặc t.")