# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:48:59 2024

@author: ADM
"""

# Nhập chuỗi giờ/phút/giây 
thoi_gian = input("Nhập giờ/phút/giây (ví dụ: 1h8p8s): ")
tong_giay = 0
# Tìm số giờ 
if 'h' in thoi_gian:
    gio = int(thoi_gian.split('h')[0])
    tong_giay += gio * 3600
# Tìm số phút 
if 'p' in thoi_gian:
    phut = int(thoi_gian.split('p')[0].split('h')[-1])
    tong_giay += phut * 60
# Tìm số giây 
if 's' in thoi_gian:
    giay = int(thoi_gian.split('s')[0].split('p')[-1])
    tong_giay += giay
print("số giây là: ", tong_giay) 