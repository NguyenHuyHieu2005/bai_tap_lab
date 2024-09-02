# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:12:25 2024

@author: ADM
"""
#nhập vào bán kính hình tròn 
R = int(input("nhập bán kính hình tròn: "))
pi = 3.14

#tính toán 
chuvi = 2 * pi * R 
dientich =  pi * R ** 2

#in kết quả
print(f"chu vi hình  với bán kính {R} là {chuvi}")
print(f"diện tích hình tròn với bán kính {R} là {dientich}")