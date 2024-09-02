# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:00:25 2024

@author: ADM
"""

chu = input("Nhập một chữ cái: ") 

if chu.islower():
    chu = chu.upper()
else:
    chu = chu.lower()

print("Chữ cái sau khi chuyển đổi là:", chu )