# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:52:08 2024

@author: ADM
"""

#tính từng phần
p1 = (32) ** 0.2 
p2 = ((1 / 64) ** (-0.25))
p3 = ((8 / 27)**(1 / 3 ))

#giá trị của 
A = p1  - (p2)  + p3 
# Làm tròn 3 chữ số sau dấu thập phân
number = A 
rounded = round(number, 3)
print(f"Số sau khi làm tròn 3 chữ số: {rounded}")