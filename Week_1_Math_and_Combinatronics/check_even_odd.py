
#* Với bài toán kiểm tra số chẵn lẻ, ta không chỉ áp dụng phần thuật toán là kiểm tra chia hết hay không, mà còn có thêm các hướng tiếp cận khác, ở đây là: 

#? 1. Naive
#* Thuật toán này sẽ kiểm tra phần dư của 2 số sau khi chia cho 2

def isEven(n):
    remainder = n % 2
    
    if remainder == 0:
        return True
    else:
        return False


#? 2. Bitwise
#* Bit cuối cùng của tất cả các số lẻ LUÔN LUÔN là 1, trong khi bit cuối của các số chẵn luôn luôn là 0, vì vậy, khi sử dụng toán tử AND với 1 cho 1 số, số lẻ sẽ trả về 1, còn số chẵn thì sẽ trả về 0

#* Ví dụ: kiểm tra xem 15 có phải là số lẻ hay số chẵn, tiến hành thao tác bit
#* 15 -> 1111 & 0001 = 0001 --> là số lẻ
#* 44 -> 101100 & 000001 = 000000 -> là số chẵn

def isEven(n):
    if (n & 1) == 0:
        return True
    else:
        return False 
