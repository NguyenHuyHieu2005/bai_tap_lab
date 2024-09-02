# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:05:22 2024

@author: ADM
"""

a = int(input("nhap so thu nhat: "))
b = int(input("nhap so thu hai: "))

phannguyen = a // b 
phandu = a % b 

print(f"Kết quả chia lấy phần nguyên của {a} cho {b} là: {phannguyen}")
print(f"Kết quả chia lấy phần dư của {a} cho {b} là: {phandu}")