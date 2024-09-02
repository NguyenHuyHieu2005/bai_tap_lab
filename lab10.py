# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:46:34 2024

@author: ADM
"""

N = (input("nhập vào biển số xe của bạn(vd 2 3 4 5): "))

tong = int( N[0]) + int(N[1]) + int(N[2]) + int(N[3])
sonut = tong % 10
print("Số nút của biển số là:", sonut )