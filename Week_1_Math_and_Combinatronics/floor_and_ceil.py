
#* Ví dụ, cho 2 số nguyên a, b (b != 0), tìm floor và ceil của phép chia 2 số nguyên đó

#? Trong đó floor (làm tròn xuống) là số nguyên lớn nhất bé hơn hoặc bằng thương của a và b
#? ceil (làm tròn lên) là số nguyên nhỏ nhất lớn hơn hoặc bằng thương của a và b

#! Approach 1: Sử dụng phép chia hiệu chỉnh dấu
def floorDiv(a, b):
    #* Toán tử `//` cho kết quả làm tròn xuống (floor)
    return a // b

def ceilDiv(a, b):
    #* Đổi dấu để thực hiện việc làm tròn lên (ceiling)
    return -(-a // b)

#! Approach 2: Sử dụng built-in functions floor() và ceil()
from math import floor, ceil
def floorDiv(a, b):
    return floor(a, b)

def ceilDiv(a, b):
    return ceil(a, b)
