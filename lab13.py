# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:49:33 2024

@author: ADM
"""

# Nhập ngày, tháng, năm sinh 
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

#1 
print("a) {}/{}/{}".format(ngay, thang, nam))
print("b) {}/{}/{}".format(ngay, thang, str(nam)[-2:]))
print("c) {}/{}/{}".format(nam, thang, ngay))

# nhập lại ngày, tháng, năm theo thứ tự khác
nam = int(input("Nhập lại năm: "))
thang = int(input("Nhập lại tháng: "))
ngay = int(input("Nhập lại ngày: "))

# Xuất lại theo định dạng ngược
print("a) {}/{}/{}".format(ngay, thang, nam))
print("b) {}/{}/{}".format(ngay, thang, str(nam)[-2:]))
print("c) {}/{}/{}".format(nam, thang, ngay))