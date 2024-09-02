# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:27:16 2024

@author: ADM
"""

A = float(input("nhap vao can nang cua ban: "))
B = float(input("nhap vao chieu coa cua ban: "))
BMI = A / B**2 
lmtron = BMI
BMI = round(lmtron, 1)
print("chi so BMI cua ban la", BMI)
if BMI < 18.5:
    print("ban thieu can")
elif 18.5 < BMI < 24.9:
    print("nguoi dep! ban that can doi")
elif 25 < BMI < 29.9:
    print("ban thua can")
elif 30 < BMI < 34.9:
    print("ban beo phi")
else:
    print(" ban la nguoi khong lo ")