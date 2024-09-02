# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:54:22 2024

@author: ADM
"""

time_input = input("Nhập vào giờ, phút và giây (định dạng hh:mm:ss): ")
hh , mm , ss = map(int , time_input.split(":"))
# Kiểm tra xem giờ, phút, giây có hợp lệ không
if 0 <= hh <= 24 and 0 <= mm < 60 and 0 <= ss < 60:
    print(" giờ phút hoặc giây không hợp lệ.")