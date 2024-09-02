# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 22:52:08 2024

@author: ADM
"""

import math
#nhap hai so a,b 
a = float(input("nhap vao gia tri a: "))
b = float(input("nhap vao gia tri b: "))
ab = a*b

#tinh tung gia tri 
can3_a = math.pow(a,1/3)
can3_b = math.pow(b,1/3)
can3_ab = math.pow(ab,1/3)
n =(a + b) / can3_a + can3_b 

#tinh tung thanh phan 
A = n - can3_ab 
B = (can3_a - can3_b)**2

#ket qua
dapan = A / B
print("dap an la: ", dapan)
dapan = round(dapan, 3)
print("Số sau khi làm tròn 3 chữ số: ", dapan)
