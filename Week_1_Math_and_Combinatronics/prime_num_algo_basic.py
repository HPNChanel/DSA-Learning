
#* Thuật toán cơ bản: kiểm tra số nguyên tố
#* Sử dụng thuật toán tối ưu: Square Root Check
#? Ở thuật toán này, ta chỉ cần kiểm tra đến căn bậc 2 của n vì nếu n có một ước lớn hơn căn bậc 2 của n, thì ƯỚC NHỎ HƠN TƯƠNG ỨNG PHẢI nhỏ hơn căn bậc 2 của n, vì vậy nếu không có số nào từ 2 đến căn bậc 2 của n mà n chia hết, thì n sẽ là số nguyên tố
import math


def isPrime(n):
    if n <= 1:
        return False

    if n == 2 or n == 3:
        return True
    
    #* Kiểm tra xem n có chia hết cho 2 và 3 hay không
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    #* Sử dụng vòng while, và kiểm tra từ 5 đến sqrt(n), bước nhảy là 6
    i = 5
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6
    
    return True


n = 11

if(isPrime(n)): 
    print("true")
else:
    print("false")